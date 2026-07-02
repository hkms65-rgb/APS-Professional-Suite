from aps.platform import build_default_kernel
from aps.kernel import KernelStatus

def test_kernel_starts():
    k=build_default_kernel(); k.start(); assert k.status == KernelStatus.RUNNING

def test_modules_registered():
    k=build_default_kernel()
    assert k.registry.get('market.intelligence').name == 'Market Intelligence'
    assert k.registry.get('realestate.facilities').name == 'Real Estate & Facilities'
