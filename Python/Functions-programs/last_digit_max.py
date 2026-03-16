def last_digit_max(n1,n2) :

    return n1 if n1%10 > n2%10 else n2

print(last_digit_max(401,700))