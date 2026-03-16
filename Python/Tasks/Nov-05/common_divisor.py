def common_div(n) :

    divisors = []

    for i in range (1,n):

        if n%i == 0 :

            divisors.append(i)
        
    return divisors

    
print(common_div(10))