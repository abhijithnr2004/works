VOWELS = "aeiou"

string = "programming"

vowels_list = [ch for ch in string if ch.casefold() in VOWELS]

print(vowels_list)