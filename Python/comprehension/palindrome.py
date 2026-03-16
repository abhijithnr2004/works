words = ["cat","act","madam","dam","malayalam"]

palindrome = { w for w in words if w==w[::-1]}

print("palindrome words : ",palindrome)