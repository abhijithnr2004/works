def first_recursive_character(word) :

    wc = {}

    for ch in word :

        if ch in wc :

            return ch

        else :

            wc[ch] = 1

    return None

print(first_recursive_character("balloon"))