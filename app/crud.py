from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def create_autotq(db: AsyncSession, autotq: schemas.AutoTQCreate):
    # Check if the serial_number already exists
    result = await db.execute(select(models.AutoTQ).filter(models.AutoTQ.serial_number == autotq.serial_number))
    existing = result.scalar_one_or_none()

    if existing:
        raise ValueError(f"Serial number {autotq.serial_number} already exists.")

    # Create a new record
    db_autotq = models.AutoTQ(
        serial_number=autotq.serial_number,
        model_name=autotq.model_name
    )
    db.add(db_autotq)
    await db.commit()
    await db.refresh(db_autotq)
    return db_autotq


async def get_autotq(db: AsyncSession, autotq_id: int):
    """Fetches an AutoTQ record by ID."""
    result = await db.execute(select(models.AutoTQ).filter(models.AutoTQ.id == autotq_id))
    return result.scalar_one_or_none()  # Return the first result or None
