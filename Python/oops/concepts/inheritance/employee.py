class Employee :

    id : str

    dept : str

    salary : int

    def __init__(self,id,dept,salary):

        self.id = id

        self.dept = dept

        self.salary = salary

    def display(self) :

        print(f"ID : {self.id} Department : {self.dept} Salary : {self.salary}")

class Developer(Employee):

    programming_language : str

    framework : str

    def __init__(self, id, dept, salary,programming_language,framework):

        super().__init__(id, dept, salary)

        self.programming_language = programming_language

        self.framework = framework

    def disp(self) :

        super().display()

        print(f"programming Language : {self.programming_language} framework : {self.framework}")

developer_instance1 = Developer("E001","hr","30000","Python","Django")


developer_instance1.disp()  
        