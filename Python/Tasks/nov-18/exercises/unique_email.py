emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@outlook.com", "b@yahoo.com"]

email_count = {}

for email in emails:

    if email in email_count:
        email_count[email] += 1
        
    else:
        email_count[email] = 1


unique_email = [key for key in email_count if email_count[key] == 1]

duplicate_email = [key for key in email_count if email_count[key] != 1]

print(f"Unique email : {unique_email}")

print(f"Duplicate email : {duplicate_email}")