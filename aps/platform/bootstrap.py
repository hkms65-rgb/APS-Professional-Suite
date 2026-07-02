from aps.kernel import Kernel
from aps.kernel.module import ModuleDescriptor, ModuleState, ModuleCategory
MODULES=[
('core.kernel','Enterprise Kernel','foundation','complete','Core runtime and module registry.'),
('market.intelligence','Market Intelligence','intelligence','active','SynthoSurvey market intelligence module.'),
('realestate.facilities','Real Estate & Facilities','industry','ready','Properties, leasing, maintenance, assets, and facilities.'),
('crm','CRM','business','ready','Customers, leads, accounts, and opportunities.'),
('finance','Finance','business','ready','Budgets, costs, ledgers, payables and receivables.'),
('hr','HR','business','ready','Employees, roles, payroll, attendance and performance.'),
('warehouse.logistics','Warehouse & Logistics','industry','ready','Inventory, 3PL, transport and fulfillment.'),
('manufacturing','Manufacturing','industry','ready','Production, recipes, batch control and quality.'),
('procurement','Procurement','business','ready','RFQs, vendors, contracts and sourcing.'),
('ai.studio','AI Studio','studio','ready','Agents, automations, prompts and knowledge.'),
('workflow.automation','Workflow & Automation','foundation','ready','Rules, approvals, events and jobs.'),
('administration','Administration','administration','ready','Users, tenants, configuration and system health.')
]
def build_default_kernel():
    k=Kernel()
    for mid,name,cat,state,summary in MODULES:
        k.register_module(ModuleDescriptor(id=mid,name=name,category=ModuleCategory(cat),state=ModuleState(state),summary=summary))
    return k
