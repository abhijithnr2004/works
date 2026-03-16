age = int(input("Enter age: "))

if age >= 18 :
    result = input("Is test passed (y/n):")

    if result == "y" :
        print("License approved")

    else :
        print("Test not cleared")

else :
    print("Not eligible due to age")
