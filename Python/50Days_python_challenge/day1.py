def divide_or_square(number):
    if number % 5 == 0:
        return round(number**.5)
    else:
        return number % 5


print(divide_or_square(101))