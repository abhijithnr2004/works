arr = [100,200,300,110,210,200,110,110,100]

new_arr = []

for n in arr :

    freq = arr.count(n)

    if(freq>1) and n not in new_arr :

        new_arr.append(n)

print(new_arr)