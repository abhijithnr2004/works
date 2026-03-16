age = int(input("Enter age : "))

if age < 18 :

    raise Exception("Invalid Age")

else :

    print("Eligible for voting")