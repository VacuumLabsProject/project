import time
import calculating_pressure


class Air:
    def __init__(self, pressure):
        self.pressure = pressure


class Chamber:
    def __init__(self, air):
        self.air = air


class Valve:
    def __init__(self):
        # self.connection_with_chamber: Chamber = None
        # self.connection_with_pump: Pump = None
        # self.connection_between_pumps: Pump = None
        self.state = "close"

    def open(self):
        self.state = "open"

    def close(self):
        self.state = "close"


class Pump:
    def __init__(self, type_of_pump,
                 valve_to_chamber,
                 valve_between_pumps,
                 chamber):
        self.type = self.__compute_type(type_of_pump)
        self.valve_to_chamber = valve_to_chamber
        self.valve_between_pump = valve_between_pumps
        self.chamber = chamber
        valve_to_chamber.connection_with_chamber = chamber

    def __compute_type(self, type_of_pump):
        if type_of_pump == "forevac":
            return "forevac"
        elif type_of_pump == "turbomolec":
            return "turbomolec"

    def start_pump(self, time, p0):
        if self.type == "forevac":
            p = calculating_pressure.calculating_pressure(p0, time, name="forvacuum")
            return p

        elif self.type == "turbomolec":
            p = calculating_pressure.calculating_pressure(p0, time, name="turbomolec")
            return p

        else:
            print "something does not connected"

    # pump.start_pump()
    # pump2.start_pump()
    # valve_between_chamber_and_pump_2.open()
    # pump2.start_pump()
