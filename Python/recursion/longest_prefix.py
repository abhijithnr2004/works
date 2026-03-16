words = ["fly","flying","flight"]

prefix = []

for w in words :

    for c in w :

        if c in w and c in words[w] :

            prefix.append(c)

print(prefix)