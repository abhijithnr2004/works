file_path = "C:\\Users\\abhij\\OneDrive\\Desktop\\development-journey-py\\python-works\\file-operations\\numbers.txt"

fr = open(file_path, "r")

nums = [int(line.rstrip("\n")) for line in fr]

even = [n for n in nums if n % 2 == 0]
odd = [n for n in nums if n % 2 != 0]

print("even numbers ",even)
print("odd numbers ",odd)




# perfect numbers
perfect_numbers = []

for num in nums:
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        perfect_numbers.append(num)

print("perfect numbers : ",perfect_numbers)



# last digit using modulus
last_digits_mod = [n % 10 for n in nums]

print("last digit using modulus :",last_digits_mod)



# last digit using slicing

last_digits = [line.strip()[-1] for line in fr if line.strip() != ""]

print("last digit using slicing",last_digits_mod)




