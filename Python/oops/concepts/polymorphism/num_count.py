class NumberCount :

    def solution(*args,**Kwargs) :

        count = 0

        value = int(Kwargs.get("Value"))

        for num in args :

            if num == value :

                count += 1

        if count == 0 :

            print("number not present")

        else :

            print("Number count : ",count)

nc_instance = NumberCount()

nc_instance.solution(10,20,30,10,Value="10")
