from armi import interfaces
from armi import runLog
from armi.reactor.flags import Flags


class ThermalInterface(interfaces.Interface):
    name = "dummyTH"

    def interactEveryNode(self, cycle=None, timeNode=None):
        runLog.info("Computing idealized flow rate")
        for assembly in self.r.core:
            runThermalHydraulics(assembly, self.cs)


def runThermalHydraulics(assembly, cs):
    massFlow = computeIdealizedFlow(assembly, cs)
    computeAxialCoolantTemperature(assembly, massFlow, cs)


def computeIdealizedFlow(a, cs):
    # compute required mass flow rate in assembly to reach target outlet temperature
    # mass flow rate will be constant in each axial region, regardless of coolant
    # area (velocity may change)
    coolants = a.getComponents(Flags.COOLANT)

    # use ARMI material library to get heat capacity for whatever the user has
    # defined the coolant as
    tempAvg = (cs["outletInC"] + cs["inletInC"]) / 2.0
    coolantProps = coolants[0].getProperties()
    heatCapacity = coolantProps.heatCapacity(Tc=tempAvg)

    deltaT = cs["outletInC"] - cs["inletInC"]
    massFlowRate = a.calcTotalParam("power") / (deltaT * heatCapacity)
    return massFlowRate


def computeAxialCoolantTemperature(a, massFlow, cs):
    """Compute block-level coolant inlet/outlet/avg temp and velocity."""
    # solve Qdot = mdot * Cp * dT for dT this time
    inlet = cs["inletInC"]
    for b in a:
        b.p.THcoolantInletT = inlet
        coolant = b.getComponent(Flags.COOLANT)
        coolantProps = coolant.getProperties()
        heatCapacity = coolantProps.heatCapacity(Tc=inlet)
        deltaT = b.p.power / (massFlow * heatCapacity)
        outlet = inlet + deltaT
        b.p.THcoolantOutletT = outlet
        b.p.THcoolantAverageT = (outlet + inlet) / 2.0
        # fun fact: could iterate on this to get
        # heat capacity properties updated better
        # get flow velocity too
        # V [m/s] = mdot [kg/s] / density [kg/m^3] / area [m^2]
        b.p.THaveCoolantVel = (
            massFlow
            / coolantProps.density(Tc=b.p.THcoolantAverageT)
            / coolant.getArea()
            * 100 ** 2
        )
        inlet = outlet
