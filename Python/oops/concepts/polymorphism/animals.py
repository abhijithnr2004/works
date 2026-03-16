class Animal :

    def __init__(self,name):

        self.name = name

    def sound(self) :

        print(self.name,"sound")

class Dog(Animal) :

    def __init__(self, name):
        super().__init__(name)

    def sound(self) :

        print(self.name,"bark")    

class Lion(Animal) :

    def __init__(self, name):
        super().__init__(name)

    def sound(self) :

        print(self.name,"Roar")  

dog_instance = Dog("pug")

lion_instance = Lion("Lion")

dog_instance.sound()

lion_instance.sound()