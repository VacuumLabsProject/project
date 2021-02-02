import core


# creating the vacuum system and connecting its elements
class VacuumSystem:
    def __init__(self, pressure):
        self.air = core.Air(pressure)
        self.chamber = core.Chamber(self.air)
        self.valve3 = core.Valve()
        self.valve2 = core.Valve()
        self.valve1 = core.Valve()
        self.pump = core.Pump("forevac", self.valve3, None, self.chamber)
        self.pump2 = core.Pump("turbomolec", self.valve1,
                               self.valve2, self.chamber)

