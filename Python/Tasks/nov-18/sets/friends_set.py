friend1 = {"cricket", "football", "hockey"}
friend2 = {"tennis", "football", "cricket"}

like_by_both = friend1.intersection(friend2)

friend1_unique = friend1.difference(friend2) 

friend2_unique = friend2.difference(friend1) 

unique_sports = friend1_unique.union(friend2_unique)

print(f"Uniques sports = {unique_sports}")

print(f"Like by both = {like_by_both}")