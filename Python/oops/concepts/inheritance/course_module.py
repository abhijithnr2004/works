class Course :

    course_name : str

    def __init__(self,course_name):

        self.course_name = course_name
        

    def display(self) :

        print("Course name : ",self.course_name)

class Module(Course) : 

    module : str

    def __init__(self, course_name,module):

        super().__init__(course_name)

        self.module = module

    def display(self) :

        super().display()

        print("Module : ",self.module)

class Lesson(Module) :

    lesson : str

    def __init__(self, course_name, module,lesson):

        super().__init__(course_name, module)

        self.lesson = lesson

    def display(self):

        super().display()
        
        print("Lesson : ",self.lesson)

lesson_instance = Lesson("Python","OOPS","inheritance")

lesson_instance.display()



    
    