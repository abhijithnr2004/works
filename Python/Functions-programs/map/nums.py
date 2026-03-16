lst =[4,5,6,7]

square = list(map(lambda n : n**2,lst))

cube = list(map(lambda num : num**3,lst))

add_five = list(map(lambda n : n+5,lst))

print("Squares : ",square)
print("Cubes : ",cube)
print("5 added : ",add_five)