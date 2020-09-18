from armi import interfaces
from armi.reactor.flags import Flags
from armi import runLog

# hard coded inlet/outlet temperatures
# NOTE: can make these user settings
inletInC = 360.0
outletInC = 520.0


class ThermalInterface(interfaces.Interface):
    name = "dummyTH"

    def interactEveryNode(self, cycle=None, timeNode=None):
        runLog.info("Computing idealized flow rate")
        for assembly in self.r.core:
            runThermalHydraulics(assembly)


def runThermalHydraulics(assembly):
    massFlow = computeIdealizedFlow(assembly)
    computeAxialCoolantTemperature(assembly, massFlow)


def computeIdealizedFlow(a):

    # compute required mass flow rate in assembly to reach target outlet temperature
    # mass flow rate will be constant in each axial region, regardless of coolant
    # area (velocity may change)
    coolants = a.getComponents(Flags.COOLANT)
    coolantMass = sum([c.getMass() for c in coolants])

    # use ARMI material library to get heat capacity for whatever the user has
    # defined the coolant as
    tempAvg = (outletInC + inletInC) / 2.0
    coolantProps = coolants[0].getProperties()
    heatCapacity = coolantProps.heatCapacity(Tc=tempAvg)

    deltaT = outletInC - inletInC
    massFlowRate = a.calcTotalParam("power") / (deltaT * heatCapacity)
    return massFlowRate


def computeAxialCoolantTemperature(a, massFlow):
    """Compute block-level coolant inlet/outlet/avg temp and velocity."""
    # solve q''' = mdot * Cp * dT for dT this time
    inlet = inletInC
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
