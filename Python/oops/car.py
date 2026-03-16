class Car :

    name : str
    brand : str
    price : int
    color : str

    def set_car(self,name,brand,price,color) :

        self.name = name
        self.brand = brand
        self.price = price
        self.color = color

    def display(self):
        print("name : ",self.name)
        print("Brand : ",self.brand)
        print("Price : ",self.price)
        print("Color : ",self.color)

car_instance1 = Car()

car_instance1.set_car("swift","suzuki",50000,"white")

car_instance1.display()


