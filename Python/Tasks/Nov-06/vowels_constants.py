def display_vowel_and_cosonant_count(word) :

    VOWELS = "AEIOUaeiou"
    
    vowels_count = 0

    constants_count = 0

    for ch in word :

        if ch.isalpha() :

            if ch in VOWELS :

                vowels_count += 1

            else :

                constants_count += 1

    print("vowels :", vowels_count)

    print("consonants :", constants_count)

display_vowel_and_cosonant_count("Hello123")
