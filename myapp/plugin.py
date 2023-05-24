from armi import interfaces
from armi import plugins
from armi.interfaces import STACK_ORDER as ORDER
from armi.settings.fwSettings.globalSettings import CONF_VERSIONS

from myapp import __version__
from myapp import fluxSolver
from myapp import settings
from myapp import thermalSolver


class DummyPhysicsPlugin(plugins.ArmiPlugin):
    @staticmethod
    @plugins.HOOKIMPL
    def exposeInterfaces(cs):
        DummyPhysicsPlugin.setVersionInSettings(cs)

        kernels = [
            interfaces.InterfaceInfo(ORDER.FLUX, fluxSolver.FluxInterface, {}),
            interfaces.InterfaceInfo(
                ORDER.THERMAL_HYDRAULICS, thermalSolver.ThermalInterface, {}
            ),
        ]
        return kernels

    @staticmethod
    @plugins.HOOKIMPL
    def defineSettings():
        return settings.defineSettings()

    @staticmethod
    @plugins.HOOKIMPL
    def defineSettingsValidators(inspector):
        return settings.defineValidators(inspector)

    @staticmethod
    @plugins.HOOKIMPL
    def defineCaseDependencies(case, suite):
        DummyPhysicsPlugin.setVersionInSettings(case.cs)

    @staticmethod
    def setVersionInSettings(cs):
        """Helper method to set the version correctly in the Settings file."""
        cs[CONF_VERSIONS]["armi-example-app"] = __version__
