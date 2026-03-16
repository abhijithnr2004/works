n1 = int(input("Enter number 1 : "))

n2 = int(input("Enter number 2 : "))

try :

    result = n1/n2

    print(result)

except Exception as e :

    num2 = int(input("Enter number 2 : "))
    
    result = n1/n2

    print(result)   

finally :

    print("Sending text message....")