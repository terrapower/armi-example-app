from armi import materials
from armi.utils.units import getTc


class Sodium(materials.Sodium):
    def heatCapacity(self, Tk=None, Tc=None):
        """Sodium heat capacity in J/kg-K"""
        Tc = getTc(Tc, Tk)
        # not even temperature dependent for now
        return 1.252
