from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    upc: str
    name: str
    brand: str
    category: str
    package_count: int | None = None
    unit_size: Decimal | None = None
    unit_of_measure: str | None = None
    container_type: str | None = None
    barcode_level: str | None = None
    notes: str | None = None


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
