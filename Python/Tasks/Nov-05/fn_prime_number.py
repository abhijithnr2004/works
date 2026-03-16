def is_prime(n) :

    flag = True

    if n<2 :
        return False

    for i in range(2,n) :

        if n%i == 0 :

            flag = False
            break

    return flag

print(is_prime(7))