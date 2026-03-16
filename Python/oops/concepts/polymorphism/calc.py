class Calc :

    def add(self,*args) :

        print(sum(args))

    def mult(self,*args) :

        product = 1

        for n in args :

            product *= n
        
        print(product)

        

    
calc_instance = Calc()

calc_instance.add(10,20,20)

calc_instance.mult(10,7)

calc_instance.mult(10,2,3)


        
