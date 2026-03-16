all_users = {"sachin","dravid","laxman","ganguly","sreenath","zaheer","dhoni","yuvi","kaif"}

sachin_friends = {"dravid","laxman","ganguly"}

dhoni_friends = {"dravid","laxman","yuvi","kaif"}

suggestion = all_users.difference(sachin_friends)

# suggestion = all_users ^ sachin_friends

suggestion.remove("sachin")

print("friend suggestion = ",suggestion)

mutual = sachin_friends.intersection(dhoni_friends)

print("mutual friends = ",mutual)

dhoni_suggestion = all_users.symmetric_difference(dhoni_friends)

dhoni_suggestion.remove("dhoni")

print("suggestion for dhoni =",dhoni_suggestion)