print("ICECREAM SHOP")

print("Options")

print("""1. Chocolate
2. Vanilla
3. Strawberry
4. Butterscotch""")

choice = int(input("Enter your flavor choice (1-4): "))

match choice:
    case 1:
        print("You chose Chocolate flavor.")
    case 2:
        print("You chose Vanilla flavor.")
    case 3:
        print("You chose Strawberry flavor.")
    case 4:
        print("You chose Butterscotch flavor.")
    case _:
        print("Invalid Choice")