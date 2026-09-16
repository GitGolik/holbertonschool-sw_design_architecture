#!/usr/bin/env python3


class Bus:
    def mode(self):
        return "road"

class Train:
    def mode(self):
        return "rails"

class Bike:
    def mode(self):
        return "lane"

class Scooter:
    def mode(self):
        return "scooter_lane"

class VehicleFactory:
    _registry = {
        "bus": Bus,
        "train": Train,
        "bike": Bike,
    }

    @classmethod
    def register_kind(cls, name, vehicle_class):
        cls._registry[name] = vehicle_class

    @classmethod
    def create(cls, kind):
        vehicle_class = cls._registry.get(kind)

        if vehicle_class is None:
            raise ValueError(f"Unknown vehicle kind: {kind}")

        return vehicle_class()

def main():
    factory = VehicleFactory()

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    factory.register_kind("scooter", Scooter)

    print(factory.create("scooter").mode())

if __name__ == "__main__":
    main()
