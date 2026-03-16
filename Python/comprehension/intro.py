#easy to create list,tuple ,set,dict from a sequence

"""
syntax :
result = [return iteration condition] - list comprehension
result = {return iteration condition} - list comprehension
result = tuple(return iteration condition) - list comprehension
result = [return iteration condition] - list comprehension

"""

arr = [3,4,5,6,7,8]

cubes = [ num**3 for num in arr ]

print(cubes)