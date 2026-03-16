lst = [10,11,12,13,14,15,8,3,2,1]

evens = list(filter(lambda n : n%2==0,lst))

print("Even numbers : ",evens)

odd = list(filter(lambda n : n%2!=0,lst))

print("Odd numbers : ",odd)

gt_5 = list(filter(lambda n : n>5,lst))

print("Greater than 5 : ",gt_5)

