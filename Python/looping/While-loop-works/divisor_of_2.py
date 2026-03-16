num1 = int(input("Enter number : "))

num2 = int(input("Enter number 2 : "))

small =0

if num1 < num2 :
    small = num1
else :
    small = num2

i = 1

while i <= small :
     
     if i%num1 == 0 and i%num2 == 0:
         print(i)
     i+=1


