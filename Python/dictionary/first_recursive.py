word = "balloon"

wc = {}

for ch in word :

    if ch in wc.keys() :

        print("First recursive character : ",ch) 
        
        break
    
    else :

        wc[ch] = 1