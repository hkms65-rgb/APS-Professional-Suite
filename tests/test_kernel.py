from aps.kernel import Kernel, KernelStatus, ModuleDescriptor, ModuleState


def test_kernel_starts_from_created_state():
    kernel = Kernel()
    assert kernel.status == KernelStatus.CREATED
    kernel.start()
    assert kernel.status == KernelStatus.RUNNING


def test_kernel_registers_modules():
    kernel = Kernel()
    kernel.register_module(ModuleDescriptor(name="Enterprise Kernel", state=ModuleState.READY))
    assert "Enterprise Kernel" in kernel.module_summary()


def test_module_dependency_readiness():
    module = ModuleDescriptor(name="Platform Runtime", dependencies=("Enterprise Kernel",))
    assert module.is_dependency_ready({"Enterprise Kernel"})
    assert not module.is_dependency_ready(set())
