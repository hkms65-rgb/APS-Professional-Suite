class RealEstateService:
    def __init__(self): self.properties=[]
    def create_property(self,name,property_type,area_sqm,location,monthly_revenue=0):
        p={'name':name,'property_type':str(property_type),'area_sqm':area_sqm,'location':location,'monthly_revenue':monthly_revenue}
        self.properties.append(p); return p
    def portfolio_summary(self):
        monthly=sum(float(p.get('monthly_revenue',0)) for p in self.properties)
        return {'property_count':len(self.properties),'monthly_revenue':monthly,'annualized_revenue':monthly*12}
