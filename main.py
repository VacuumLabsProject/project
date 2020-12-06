import time


class Air:
    def __init__(self, pressure):
        self.pressure = pressure


class Chamber:
    def __init__(self, air: Air):
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
    def __init__(self, type_of_pump: str,
                 valve_to_chamber: Valve,
                 valve_between_pumps: Valve or None,
                 chamber: Chamber):
        self.type = self.__compute_type(type_of_pump)
        self.valve_to_chamber = valve_to_chamber
        self.valve_between_pump = valve_between_pumps
        self.chamber = chamber
        valve_to_chamber.connection_with_chamber = chamber

    def __compute_type(self, type_of_pump: str):
        if type_of_pump == "forevac":
            return "forevac"
        elif type_of_pump == "turbomolec":
            return "turbomolec"

    def start_pump(self):
        if self.valve_between_pump is None:
            print("pre vacuum")
            while chamber.air.pressure > 1000:
                chamber.air.pressure -= 1
                print(chamber.air.pressure)
                time.sleep(1)

        elif self.valve_to_chamber.state == "open" and self.valve_between_pump.state == "open":
            print("main vacuum")
            while chamber.air.pressure > 990:
                chamber.air.pressure -= 1
                print(chamber.air.pressure)
                time.sleep(2)

        else:
            print("что-то не соединено")


if __name__ == '__main__':
    air = Air(1010)
    chamber = Chamber(air)
    valve_between_chamber_and_pump = Valve()
    valve_between_pumps = Valve()
    valve_between_chamber_and_pump_2 = Valve()
    pump = Pump("forevac", valve_between_chamber_and_pump, None, chamber)
    pump2 = Pump("turbomolec", valve_between_chamber_and_pump_2,
                 valve_between_pumps, chamber)
    valve_between_chamber_and_pump.open()
    valve_between_pumps.open()
    pump.start_pump()
    pump2.start_pump()
    valve_between_chamber_and_pump_2.open()
    pump2.start_pump()

