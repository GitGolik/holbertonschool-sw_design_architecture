#!/usr/bin/env python3


class Beverage:
    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Coffee(Beverage):
    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    coffee_with_milk = MilkDecorator(Coffee())
    print(
        coffee_with_milk.description(),
        coffee_with_milk.cost(),
    )

    coffee_with_sugar_and_milk = MilkDecorator(
        SugarDecorator(Coffee())
    )
    print(
        coffee_with_sugar_and_milk.description(),
        coffee_with_sugar_and_milk.cost(),
    )

    coffee_with_sugar_milk_and_caramel = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(Coffee())
        )
    )
    print(
        coffee_with_sugar_milk_and_caramel.description(),
        coffee_with_sugar_milk_and_caramel.cost(),
    )


if __name__ == "__main__":
    main()
