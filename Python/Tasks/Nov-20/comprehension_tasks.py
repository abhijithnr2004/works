# 1. squares of even numbers

nums = [1,2,3,4,5,6]

ev_sq = [ n*n for n in nums if n % 2 == 0 ]

print(ev_sq)



# 2. words longer than 5 chars

s = "Python programming is very interesting"

long_words = [ w for w in s.split() if len(w) > 5 ]

print(long_words)



# 3. marks to grades

marks = {"Aju":92, "Binu":76, "Chandru":64}

grade_map = { n : ("A" if m>=90 else "B" if m>=75 else "C") for n,m in marks.items() }

print(grade_map)



# 4. unique vowels

word = "communication"

vowels = "aeiou"

v_set = { ch for ch in word if ch in vowels }

print(v_set)



# 5. tuples (n, cube) divisible by 3

cubes = [ (n, n**3) for n in range(1,31) if n % 3 == 0 ]

print(cubes)



# 6. reverse each word

words = ["python","django","react"]

rev = [ w[::-1] for w in words ]

print(rev)



# 7. factorial dictionary

fact = { n : (1 if n==1 else n*1) for n in range(1,11) }

# fix factorial using loop

for k in fact :
    
    f = 1
    
    for i in range(1, k+1) :
        
        f *= i
    
    fact[k] = f

print(fact)



# 8. flatten nested list

nested = [[1,2],[3,4],[5,6]]

flat = [ x for lst in nested for x in lst ]

print(flat)



# 9. squares of odd numbers as strings

nums = [1,2,3,4,5]

odd_sq = [ str(n*n) for n in nums if n % 2 != 0 ]

print(odd_sq)



# 10. character frequency

s = "banana"

freq = { ch : s.count(ch) for ch in set(s) }

print(freq)
