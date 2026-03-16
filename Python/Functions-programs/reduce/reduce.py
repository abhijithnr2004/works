from functools import reduce

lst = [1,2,3,7,6,5]

max_num = reduce(lambda n1,n2 : n1 if n1>n2 else n2,lst)
min_num = reduce(lambda n1,n2 : n1 if n1<n2 else n2,lst)
product = reduce(lambda n1,n2 : n1*n2,lst)

print("max : ",max_num)

print("min :",min_num)

print("product : ",product)

