class Vehicle:
    def move(self):
        """
        Base method for movement. Should be overridden in subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses")


class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚤"


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
