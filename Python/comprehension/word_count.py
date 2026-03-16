words = ["am","in","on","off","in","out","off"]

wc = { w:words.count(w) for w in set(words)}

print(wc)
