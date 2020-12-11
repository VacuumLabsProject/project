import time


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

    def start_pump(self):
        if self.valve_between_pump is None:
            print("pre vacuum")
            if self.chamber.air.pressure > 1000:
                self.chamber.air.pressure -= 1
                print(self.chamber.air.pressure)
                # time.sleep(1)
                return self.chamber.air.pressure

        elif self.valve_to_chamber.state == "open" and self.valve_between_pump.state == "open":
            print("main vacuum")
            if self.chamber.air.pressure > 990:
                self.chamber.air.pressure -= 1
                print(self.chamber.air.pressure)
                time.sleep(2)
                return self.chamber.air.pressure

        else:
            print "something does not connected"

    # pump.start_pump()
    # pump2.start_pump()
    # valve_between_chamber_and_pump_2.open()
    # pump2.start_pump()
