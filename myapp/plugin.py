from armi import plugins
from armi import interfaces
from armi.interfaces import STACK_ORDER as ORDER

from myapp import fluxSolver
from myapp import thermalSolver


class DummyPhysicsPlugin(plugins.ArmiPlugin):
    @staticmethod
    @plugins.HOOKIMPL
    def exposeInterfaces(cs):
        kernels = [
            interfaces.InterfaceInfo(ORDER.FLUX, fluxSolver.FluxInterface, {}),
            interfaces.InterfaceInfo(
                ORDER.THERMAL_HYDRAULICS, thermalSolver.ThermalInterface, {}
            ),
        ]
        return kernels
