set_a = {100,200,300,400}

set_b = (10,20,30,300,400,40)



union_set = set_a.union(set_b)

print(union_set)



print(set_a.intersection(set_b))



print(set_a.difference(set_b))



set_c = {100,200,300,400,500}

set_d = {200,500}

print("superset")



print(set_c.issuperset(set_d))



print(set_d.issuperset(set_c))


print("subset")


print(set_c.issubset(set_d))


print(set_d.issubset(set_c))