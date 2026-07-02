from aps.kernel import Kernel
from aps.kernel.module import ModuleDescriptor, ModuleState, ModuleCategory

MODULES = [('core.kernel', 'Enterprise Kernel', 'foundation', 'complete', 'Core runtime and registry.'), ('market.intelligence', 'Market Intelligence', 'intelligence', 'active', 'SynthoSurvey market research module.'), ('realestate.facilities', 'Real Estate & Facilities', 'industry', 'ready', 'Portfolio, leasing, maintenance and facilities.'), ('crm', 'CRM', 'business', 'ready', 'Customers, leads and opportunities.'), ('finance', 'Finance', 'business', 'ready', 'Financial planning and accounting.'), ('hr', 'HR', 'business', 'ready', 'People and organization.'), ('warehouse.logistics', 'Warehouse & Logistics', 'industry', 'ready', 'Inventory and logistics.'), ('manufacturing', 'Manufacturing', 'industry', 'ready', 'Production and quality.'), ('ai.studio', 'AI Studio', 'studio', 'ready', 'AI agents and automations.')]

def build_default_kernel() -> Kernel:
    kernel = Kernel()
    for mid, name, cat, state, summary in MODULES:
        kernel.register_module(ModuleDescriptor(id=mid, name=name, category=ModuleCategory(cat), state=ModuleState(state), summary=summary))
    return kernel
