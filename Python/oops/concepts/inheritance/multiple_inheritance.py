class Father :

    def father_skill(self) :

        print("cricket skill")

class Mother :

    def mother_skill(self) :

        print("cooking")

class Child(Father,Mother) :

    def child_skill(self) :

        pass

child_instance = Child()

child_instance.father_skill()

child_instance.mother_skill()





    