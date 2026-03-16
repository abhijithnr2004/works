class Grandparent :

    def properties(self) :

        print("50 cent land vintage home")

class Parent(Grandparent) :

    def vehicles(self) :

        print("swift car")

class Child(Parent) :

    def gadgets(self) :

        print("iphone,laptop")

child_instance = Child()

child_instance.properties()
child_instance.vehicles()
child_instance.gadgets()
    

