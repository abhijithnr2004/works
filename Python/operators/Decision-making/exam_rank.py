mark = int(input("Enter mark out 100: "))

if mark >= 90 and mark <= 100:
    print("Distinction")
elif mark >= 40 :
        print("Pass")
elif mark >= 0 and mark < 40 :
    print("Fail")
else :
    print("Invalid entry")