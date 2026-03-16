for r in range(8,1,-1) :

    if r>4 :

        for sp in range(r,8):
            print(" ",end="")

        for star in range(4,r):
            print("*",end=" ")
        
        print()
    
    else :

        for sp in range(2,r):
            print(" ",end="")

        for star in range(r,6):
            print("*",end=" ")

        print()

