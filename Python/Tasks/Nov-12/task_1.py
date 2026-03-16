words = ["hello","hai","hello","is"]

recursive = [0] * len(words)

non_recursive = [0] * len(words)

k = 0

j = 0

for i in range(len(words)) :

    count = 0

    for c in range (i+1,len(words)) :

        if words[i] == words[c]:

                count = 1
                break
        
    if count == 0 and words[i] not in recursive :
        non_recursive[k] = words[i]
        k+=1
            

    elif words[i] not in recursive :

        recursive[j] = words[i]
        j+=1

print("Non - Recursive words = ",[non_recursive[x] for x in range(k)])

print("Recursive Words = ",[recursive[y] for y in range(j)])