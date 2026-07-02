from dataclasses import asdict
from aps.domain.realestate import Property, PropertyType
from aps.persistence import SQLiteStore

class RealEstateService:
    def __init__(self, store=None):
        self.store = store or SQLiteStore()

    def create_property(self, name: str, property_type: PropertyType, area_sqm: float, location: str, monthly_revenue: float=0.0) -> Property:
        prop = Property(name, property_type, area_sqm, location, monthly_revenue)
        data = asdict(prop); data['property_type'] = prop.property_type.value
        self.store.put('properties', prop.property_id, data)
        return prop

    def list_properties(self):
        return self.store.list('properties')

    def portfolio_summary(self):
        props = self.list_properties()
        monthly = sum(float(p.get('monthly_revenue',0)) for p in props)
        return {'property_count': len(props), 'monthly_revenue': monthly, 'annualized_revenue': monthly*12}
