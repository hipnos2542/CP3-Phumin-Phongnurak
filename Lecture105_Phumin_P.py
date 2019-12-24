class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirconditional(self):
        print("Turn on : Air")
class Car(Vehicle):
    def sayHello(self):
        print("Hello")

class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirconditional()
pickUp = PickUp()
pickUp.turnOnAirconditional()
van = Van()
van.turnOnAirconditional()
estateCar = EstateCar()
estateCar.turnOnAirconditional()