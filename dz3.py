
class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Транспортний засіб переміщається зі швидкістю {self.speed} км/год.")


class Car(Transport):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def move(self):
        print(f"Автомобіль {self.brand} їде зі швидкістю {self.speed} км/год.")


class Bicycle(Transport):
    def __init__(self, speed, type_bicycle):
        super().__init__(speed)
        self.type_bicycle = type_bicycle

    def move(self):
        print(f"Велосипед типу {self.type_bicycle} рухається зі швидкістю {self.speed} км/год.")


class Airplane(Transport):
    def __init__(self, speed, airline):
        super().__init__(speed)
        self.airline = airline

    def move(self):
        print(f"Літак авіакомпанії {self.airline} летить зі швидкістю {self.speed} км/год.")


car = Car(120, "Bugatti")
bicycle = Bicycle(25, "Спортивний")
airplane = Airplane(900, "Belavia")

car.move()
bicycle.move()
airplane.move()
