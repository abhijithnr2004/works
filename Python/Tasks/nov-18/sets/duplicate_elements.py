numbers = [1, 2, 3, 2, 4, 5, 1, 6]

duplicates = set()

nums = set()

for number in numbers:

    if number in nums:
        duplicates.add(number)

    else:
        nums.add(number)

print(f"Duplicates : {duplicates}")