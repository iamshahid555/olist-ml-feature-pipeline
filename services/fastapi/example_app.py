from typing import Dict, List, Optional
import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, JSON, create_engine, MetaData, Table
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL")  # e.g. postgresql://user:pass@host:5432/dbname
USE_SQLITE_FALLBACK = DATABASE_URL is None

if USE_SQLITE_FALLBACK:
    DATABASE_URL = "sqlite:///./example.db"

engine: Engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()

features_table = Table(
    "orders_features",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("order_id", String, unique=True, index=True, nullable=False),
    Column("features", JSON, nullable=False),
)

app = FastAPI(title="Olist Feature API", version="0.2")


class Health(BaseModel):
    status: str
    components: Dict[str, str]


class TableInfo(BaseModel):
    name: str
    rows: int
    updated_at: Optional[str] = None


class FeatureRow(BaseModel):
    order_id: str
    features: Dict[str, float]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    # create tables if using sqlite fallback
    metadata.create_all(bind=engine)
    # seed sample data if table empty
    with SessionLocal() as db:
        result = db.execute(features_table.select().limit(1)).fetchone()
        if result is None:
            sample = {"order_id": "ORDER_123", "features": {"delivery_time": 3.4, "review_score": 4.2}}
            db.execute(features_table.insert().values(**sample))
            db.commit()


@app.get("/health", response_model=Health)
def health():
    # Lightweight checks; in production expand to real probes
    components = {"kafka": "unknown", "spark": "unknown", "postgres": "unknown", "airflow": "unknown"}
    # mark postgres ok if DB reachable
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        components["postgres"] = "ok"
    except Exception:
        components["postgres"] = "unavailable"
    return {"status": "ok", "components": components}


@app.get("/tables", response_model=List[TableInfo])
def list_tables(db=Depends(get_db)):
    count = db.execute(features_table.count()).scalar() if engine.dialect.name != "sqlite" else db.execute(features_table.count()).scalar()
    return [{"name": "orders_features", "rows": int(count), "updated_at": None}]


@app.get("/features", response_model=FeatureRow)
def get_features(order_id: str, db=Depends(get_db)):
    row = db.execute(features_table.select().where(features_table.c.order_id == order_id)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="order not found")
    return {"order_id": row["order_id"], "features": row["features"]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
