arr = [3,4,12,13,14,20,22]



even_arr =[]
odd_arr = []

for n in arr :

    if n%2 == 0 :
        even_arr.append(n)
    else :
        odd_arr.append(n)

print("even numbers = ",even_arr)

print("odd numbers = ",odd_arr)