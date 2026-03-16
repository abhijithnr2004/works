def consonant_count(word) :

    VOWELS = "AEIOUaeiou"

    count = 0

    for ch in word :

        if ch not in VOWELS  and ch.isalpha() :

            count+=1

    return count

print(consonant_count("HAI"))

print(consonant_count("abHAI123"))
