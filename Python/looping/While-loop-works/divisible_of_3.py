num1 = int(input("Enter number : "))

num2 = int(input("Enter number 2 : "))

num3 = int(input("Enter number 3 : "))

small =0

if num1 < num2 and num3 :
    small = num1
elif num2 < num3 and num1 :
    small = num2
else :
    small = num3

i = 1

while i <= small :
     
    if num1%1 == 0 and num2%i == 0 and num3%i == 0:
         print(i)
    i+=1


