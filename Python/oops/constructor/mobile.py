class Mobile :

    title : str
    price : int
    brand : str
    features : str

    def __init__(self,title,price,brand,features) :
        self.title = title
        self.price = price
        self.brand = brand
        self.features = features

    def display(self) :
        print(f"mobile details : Title : {self.title},Price : {self.price},Brand : {self.brand},Features : {self.features}")


mobile1 = Mobile("Redmi Note 11",10000,"Redmi","50 mp back cam, 5500 Mah Battery")
mobile1.display()