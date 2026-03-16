for r in range (1,5):
    
    for c in range(1,8):

        if r==4 or r+c==5 or c-r==3:
            print("*",end=" ")
        else :
            print(" ",end=" ")

    print()