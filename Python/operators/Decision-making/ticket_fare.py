age = int(input("Enter your age: "))

if age > 0 :

    if age < 5 :
        print("Free ticket")

    elif age < 19 :
        print("Your ticket fair is $10")

    elif age < 61 :
        print("Your tciket fair is $20")

    elif age > 60 :
        print("Your tciket fair is $15")

else :
    print("Invalid age")

