import numpy as np

from armi import runLog
from armi import interfaces
from armi.reactor.flags import Flags


class FluxInterface(interfaces.Interface):
    name = "dummyFlux"

    def interactEveryNode(self, cycle=None, timeNode=None):
        runLog.info("Computing neutron flux and power.")
        setFakePower(self.r.core)


def setFakePower(core):
    fuelBlocks = core[0].getBlocks(Flags.FUEL)
    topFuelZ = fuelBlocks[-1].spatialLocator.getGlobalCoordinates()[2]
    bottomFuelZ = fuelBlocks[0].spatialLocator.getGlobalCoordinates()[2]
    coreMidPlane = (topFuelZ - bottomFuelZ) / 2.0 + bottomFuelZ
    center = np.array([0, 0, coreMidPlane])
    peakPower = 1e6
    mgFluxBase = np.arange(5)
    for a in core:
        for b in a:
            vol = b.getVolume()
            coords = b.spatialLocator.getGlobalCoordinates()
            r = np.linalg.norm(abs(coords - center))
            fuelFlag = 10 if b.isFuel() else 1.0
            b.p.power = peakPower / r ** 2 * fuelFlag / b.getSymmetryFactor()
            b.p.pdens = b.p.power / vol
            b.p.mgFlux = mgFluxBase * b.p.pdens
