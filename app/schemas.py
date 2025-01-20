from pydantic import BaseModel
from datetime import datetime

class AutoTQCreate(BaseModel):
    serial_number: str
    model_name: str

class AutoTQ(BaseModel):
    id: int
    serial_number: str
    model_name: str
    status: str
    created_at: datetime  # Use datetime type for proper serialization

    class Config:
        from_attributes = True
        protected_namespaces = ()  # Disables the warning
