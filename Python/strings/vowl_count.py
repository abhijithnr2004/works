def vowel_count(word) :

    count = 0

    for ch in word :

        VOWELS = "aeiouAEIOU"

        if ch in VOWELS :

            count+=1
        
    return count

print(vowel_count("programming pro"))

print(vowel_count("HAI"))
