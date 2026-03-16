A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}

common = A.intersection(B)

print("Elements common to both sets : ",common)

in_A = A.difference(B)

print("Elements present in A but not in B : ",in_A)

symmetric = A.symmetric_difference(B)

print("The symmetric difference between A and B : ",symmetric)