def gcd(n1,n2) :
 
    smallest = min(n1,n2)

    for i in range(smallest,1,-1):

        if n1%i == 0 and n2%i == 0 :
            return i
    
print(gcd(20,30))