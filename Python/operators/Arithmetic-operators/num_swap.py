num1 = int(input("Enter first nummber : ")) #100

num2 = int(input("Enter second number : ")) #200

print("values before swapping num1 =",num1,"num2 =",num2)

num1 = num1+num2 #100+200=300
num2 = num1-num2 #300-200=100
num1 = num1-num2 #300-100=200

print("values after swapping num1 =",num1,"num2 =",num2)