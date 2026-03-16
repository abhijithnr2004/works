def perfect_number(n) :
    
    sum = 0

    for i in range(1,n):
        if n%i == 0 :
            sum = sum+i
        
    return "Perfect Number" if sum == n else "Not Perfect number"

print(perfect_number(28))