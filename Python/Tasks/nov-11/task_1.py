arr = [1, 5, 7, 9, 12, 15, 16, 19, 20]

odd_count = 0

even_count = 0

for n in arr :

    if n%2 == 0:

        print("odd number = ",n)
        odd_count+=1
    
    else:

        print("Even number = ",n)
        even_count+=1

print("Count of odd numbers = ",odd_count)

print("Count of Even numbers = ",even_count)

