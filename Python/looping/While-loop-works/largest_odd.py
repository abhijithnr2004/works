num = int(input("Enter num : "))

largest_odd = 0

while num!=0 :

    dig = num % 10
    if dig%2 != 0 :
        if dig > largest_odd :
            largest_odd = dig
    num = num//10
    if num%2 != 0 :
        if num > largest_odd :
            largest_odd = num

if largest_odd==0 :
    print("no odd numbers")
else :
    print(largest_odd)


           
    