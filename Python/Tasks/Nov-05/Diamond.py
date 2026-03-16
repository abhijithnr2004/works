for r in range(1,8) :

    if r<5 :

        for sp in range(1,5-r) :
            print(" ",end="")

        for star in range(r,0,-1) :
            print("*",end=" ")

        print()

    else :

        for sp in range(4,r):
            print(" ",end="")

        for star in range(0,8-r):
            print("*",end=" ")
        
        print()