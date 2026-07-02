from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4

class PropertyType(str, Enum):
    COMMERCIAL='commercial'
    INDUSTRIAL='industrial'
    WAREHOUSE='warehouse'
    OFFICE='office'
    RETAIL='retail'

@dataclass
class Property:
    name: str
    property_type: PropertyType
    area_sqm: float
    location: str
    monthly_revenue: float = 0.0
    property_id: str = field(default_factory=lambda: str(uuid4()))

    def annualized_revenue(self) -> float:
        return self.monthly_revenue * 12
