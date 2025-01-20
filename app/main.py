from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from . import models, schemas, crud
from .database import engine, Base

# Asynchronous session maker
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

# FastAPI instance
app = FastAPI()

# Create tables asynchronously
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup_event():
    await init_db()

# Dependency to get database session
async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()

@app.post("/autotq/", response_model=schemas.AutoTQ)
async def create_autotq(autotq: schemas.AutoTQCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await crud.create_autotq(db, autotq)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))