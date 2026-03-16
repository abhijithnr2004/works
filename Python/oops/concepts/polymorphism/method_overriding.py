"""
method overriding

child class changes the behaviour of method inherited from parent class
"""

class Vehicle :

    def __init__(self,brand,title):

        self.brand = brand
        self.title = title

    def move(self) :

        print(self.title,"is moving")

class Car(Vehicle) :

    def __init__(self, brand, title):
        super().__init__(brand, title)

class Ship(Vehicle) :

    def __init__(self, brand, title):
        super().__init__(brand, title)

    def move(self):

        print(self.title,"is sailing")

car_instance = Car("Toyota","Fortuner")

ship_instance = Ship("Royal Caribbean","Icon of the sea")

car_instance.move()

ship_instance.move()
        