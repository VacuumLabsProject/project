import core


# creating the vacuum system and connecting its elements
class VacuumSystem:
    def __init__(self, pressure):
        self.air = core.Air(pressure)
        self.chamber = core.Chamber(self.air)
        self.valve_between_chamber_and_pump = core.Valve()
        self.valve_between_pumps = core.Valve()
        self.valve_between_chamber_and_pump_2 = core.Valve()
        self.pump = core.Pump("forevac", self.valve_between_chamber_and_pump, None, self.chamber)
        self.pump2 = core.Pump("turbomolec", self.valve_between_chamber_and_pump_2,
                               self.valve_between_pumps, self.chamber)

        self.valve_between_pumps.open()
