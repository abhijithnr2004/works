"""
Docstring for python-works.oops.Class-Object.method_overloading

method overloading(not supported in python)

same method name different number of parameters within a class

"""

class Calculator :

    def add(self,num1,num2) :

        print(num1+num2) 

    def add(self,num1,num2,num3) :

        print(num1+num2+num3) 

    def add(self,num1,num2,num3,num4) :

        print(num1+num2+num3+num4) 

calc_instance = Calculator()

calc_instance.add(100,200,300,400)

calc_instance.add(100,200)



    
    

