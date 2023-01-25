"""Settings related to the DummyPhysicsPlugin"""

from armi.operators.settingsValidation import Query, validateVersion
from armi.settings import setting

from myapp import __version__ as version


CONF_INLET_TEMPERATURE = "inletInC"
CONF_OUTLET_TEMPERATURE = "outletInC"
CONF_MYAPP_VERSION = "myAppVersion"


def defineSettings():
    """Define DummyPhysicsPlugin settings."""
    settings = [
        setting.Setting(
            CONF_INLET_TEMPERATURE,
            default=360.0,
            label="Inlet Temperature (Celcius)",
            description="The Inlet Temperature in C, for the TH solver.",
        ),
        setting.Setting(
            CONF_OUTLET_TEMPERATURE,
            default=520.0,
            label="Outlet Temperature (Celcius)",
            description="The Outlet Temperature in C, for the TH solver.",
        ),
        setting.Setting(
            CONF_MYAPP_VERSION,
            default="uncontrolled",
            label="Acceptable version of this app.",
            description="Valid versions of this app, that this settings file will accept.",
        ),
    ]
    return settings


def defineValidators(inspector):
    """Define validators for the DummyPhysicsPlugin settings."""
    return [
        Query(
            lambda: inspector.cs[CONF_INLET_TEMPERATURE] < 0.0,
            "The inlet temperature is below 0. This is unphysical and will result in unphysical results.",
            "",
            inspector.NO_ACTION,
        ),
        Query(
            lambda: inspector.cs[CONF_OUTLET_TEMPERATURE] < 0.0,
            "The outlet temperature is below 0. This is unphysical and will result in unphysical results.",
            "",
            inspector.NO_ACTION,
        ),
        Query(
            lambda: not validateVersion(version, inspector.cs[CONF_MYAPP_VERSION]),
            "The current application version does not match the required version in the Settings file! This run is uncontrolled!",
            "",
            inspector.NO_ACTION,
        ),
    ]
