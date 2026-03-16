class Person :

    name : str
    gender : str
    age : int

    def __init__(self,name,gender,age):

        self.name = name

        self.gender = gender

        self.age = age

    def display(self):

        print(self.name,self.gender,self.age)

class Student(Person) :

    rollno : int

    course : str

    def __init__(self, name, gender, age,rollno,course):

        super().__init__(name, gender, age)

        self.rollno = rollno

        self.course = course

    def disp(self) :

        super().display()

        print(f"Roll no : {self.rollno} course : {self.course}")

Student_instance1 = Student("Abhijith","male",21,2,"Python")

Student_instance1.disp()


        