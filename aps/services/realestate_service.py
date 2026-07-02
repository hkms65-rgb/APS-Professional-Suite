class RealEstateService:
    def __init__(self, repository=None):
        self.repository = repository
        self.properties = []

    def create_property(self, name, property_type, area_sqm, location, monthly_revenue=0):
        if self.repository is not None:
            record = self.repository.create_property(str(name), str(property_type), area_sqm, str(location), monthly_revenue)
            return {
                'id': record.id,
                'name': record.name,
                'property_type': record.property_type,
                'area_sqm': record.area_sqm,
                'location': record.location,
                'monthly_revenue': record.monthly_revenue,
            }
        property_record = {
            'name': name,
            'property_type': str(property_type),
            'area_sqm': area_sqm,
            'location': location,
            'monthly_revenue': monthly_revenue,
        }
        self.properties.append(property_record)
        return property_record

    def portfolio_summary(self):
        if self.repository is not None:
            return self.repository.portfolio_summary()
        monthly = sum(float(p.get('monthly_revenue', 0)) for p in self.properties)
        return {
            'property_count': len(self.properties),
            'monthly_revenue': monthly,
            'annualized_revenue': monthly * 12,
        }
