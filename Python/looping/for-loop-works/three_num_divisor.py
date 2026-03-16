num1 = int(input("Enter number : "))

num2 = int(input("Enter number 2 : "))

num3 = int(input("Enter number 3 : "))

small_num = min(num1,num2,num3)

for i in range(1,small_num+1) :
    if num1%i == 0 and num2%i == 0 and num3%i == 0 :
        print(i)