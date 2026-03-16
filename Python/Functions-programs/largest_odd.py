def largest_odd(n) :
    odd = 0
    while (n>0) :
        if round(n%2) != 0 :
            odd = odd + n
            return odd
            break
        else :
            n = round(n/10)

        
            
            
print(largest_odd(2e174))
    