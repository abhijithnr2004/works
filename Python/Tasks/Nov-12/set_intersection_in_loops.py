data = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]

common = data[0]

for s in data[1:]:
    common = common.intersection(s)

print(common)
