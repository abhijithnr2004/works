file_path = "python-works/Tasks/Dec-08/Instagram_Analytics.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [row for row in reader]

# print(data)

# 1 . reel post count

reel_posts = [p.get("post_id") for p in data if p.get("media_type") == "Reel"]

print("count of reel posts :",len(reel_posts))


# 2 . post with highest likes

max_likes = max([int(p.get("likes",0)) for p in data])

for p in data:

    if int(p.get("likes")) == max_likes:

        print("highest like media :", p.get("media_type"))

        print("likes :", p.get("likes"))


# 3 . all unique traffic sources

all_sources = {p.get("traffic_source") for p in data}

print("traffic sources :", all_sources)



# 4 . highest engagement rate

max_eng = max([float(p.get("engagement_rate",0)) for p in data])

for p in data:

    if float(p.get("engagement_rate")) == max_eng:

        print(f"highest engagement post : {p.get("post_id")} engagement rate : {p.get("engagement_rate")}")



# 5 . average reach of photos

total_reach = 0

photo_count = 0

for p in data:

    if p.get("media_type") == "Photo":

        total_reach += int(p.get("reach",0))

        photo_count += 1

print("avg reach of photos :", total_reach/photo_count)


# 6 . media_type : total likes

likes_sum = {}

for p in data:

    m = p.get("media_type")

    l = int(p.get("likes",0))

    if m in likes_sum:

        likes_sum[m] += l

    else:

        likes_sum[m] = l

print("likes summary :", likes_sum)


# 7 . post with most followers gained

max_f = max([int(p.get("followers_gained",0)) for p in data])

for p in data:

    if int(p.get("followers_gained")) == max_f:

        print("max follower post :", p.get("post_id"))

        print("category :", p.get("content_category"))

        print("followers gained :", p.get("followers_gained"))


# 8 . photos where hashtags is 0

high_tags = []

for p in data:

    if int(p.get("hashtags_count",0)) == 0 and p.get("media_type") == "Photo":

        high_tags.append(p.get("post_id"))

print(f"Photos with 0 hashtags : {high_tags} count : {len(high_tags)}")