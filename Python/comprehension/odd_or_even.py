arr = [1,2,3,4,5,6,7,8,9]

print("odd numbers in array : ",end="")

odd = [num for num in arr if num%2 != 0]

print(odd)

print("even numbers in array : ",end="")

even = [num for num in arr if num%2 == 0]

print(even)

print("numbers greater than five :",end = "")

num_gt_5 = [num for num in arr if num>5]

print(num_gt_5)