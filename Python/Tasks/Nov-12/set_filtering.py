nums = [1, 2, 2, 3, 4, 4, 5]

unique = set()    
duplicates = set() 

for n in nums:
    if n in unique:
        duplicates.add(n)
    else:
        unique.add(n)


result = unique - duplicates

print(result)



