import numpy as np

from armi import runLog
from armi import interfaces


class FluxInterface(interfaces.Interface):
    name = "dummyFlux"

    def interactEveryNode(self, cycle=None, timeNode=None):
        runLog.info("Computing neutron flux and power.")
        setFakePower(self.r.core)


def setFakePower(core):
    midplane = core[0].getHeight() / 2.0
    center = np.array([0, 0, midplane])
    peakPower = 1e6
    mgFluxBase = np.arange(5)
    for a in core:
        for b in a:
            vol = b.getVolume()
            coords = b.spatialLocator.getGlobalCoordinates()
            r = np.linalg.norm(abs(coords - center))
            fuelFlag = 10 if b.isFuel() else 1.0
            b.p.power = peakPower / r ** 2 * fuelFlag
            b.p.pdens = b.p.power / vol
            b.p.mgFlux = mgFluxBase * b.p.pdens
