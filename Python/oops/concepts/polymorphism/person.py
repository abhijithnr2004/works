class Person :

    def __init__(self,name,age,gender):

        self.name = name

        self.age = age

        self.gender = gender


    # def display(self) :

    #     print("name : ",self.name)
    #     print("age : ",self.age)
    #     print("gender : ",self.gender)

    @property
    def get_age(self) :

        print(self.age)

person_instance = Person("Abhi",21,"male")

person_instance.get_age

# person_instance.display() 

