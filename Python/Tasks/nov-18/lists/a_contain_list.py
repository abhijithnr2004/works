words = ["apple", "dog", "cat", "pen"]

a_contain_word_list = [w for w in words if "a" in w.casefold()]

print(a_contain_word_list)