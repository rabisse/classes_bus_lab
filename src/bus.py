class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passenger_list = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passenger_list)

    def pick_up(self, person):
        self.passenger_list.append(person)

    def drop_off(self, person):
        self.passenger_list.remove(person)

    def empty(self):
        self.passenger_list.clear()

    def pick_up_from_stop(self, bus_stop):
        for person in bus_stop.queue:
            self.pick_up(bus_stop.queue)
        bus_stop.clear()
