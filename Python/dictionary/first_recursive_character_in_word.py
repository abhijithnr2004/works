word = "a man a plan panama canal"

wc = {}

for ch in word :

    if ch.isalpha():

        if ch in wc :

            wc[ch] += 1

        else :

            wc[ch] = 1

print("recursive characters : ")

for k,v in wc.items() :

    if v>1 :

        print(k,end =",")

    
    
