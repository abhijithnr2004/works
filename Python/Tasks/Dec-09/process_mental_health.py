import csv

file_path = "python-works/Tasks/Dec-09/mental_health_social_media_dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

reader = csv.DictReader(fr)

data = [row for row in reader]



# 1 . count users in each platform

platform_count = {}

for p in data :

    plat = p.get("platform")

    if plat in platform_count :

        platform_count[plat] += 1

    else :

        platform_count[plat] = 1

print("platform wise count :", platform_count)



# 2 . lowest daily screen time

min_screen = min([int(p.get("daily_screen_time_min",0)) for p in data])

for p in data :

    if int(p.get("daily_screen_time_min")) == min_screen :

        print(f"Lowest screen time user : {p.get("person_name")} screen time : {p.get("daily_screen_time_min")}")


# 3 . sleep < 7 hours

low_sleep = [ p.get("person_name") for p in data if float(p.get("sleep_hours",0)) < 7 ]

print("count of people sleeping < 7 hrs :", len(low_sleep))



# 4 . avg social media time per platform

sm_avg = {}

count = {}

for p in data :

    plat = p.get("platform")

    time = int(p.get("social_media_time_min",0))

    if plat in sm_avg :

        sm_avg[plat] += time

        count[plat] += 1

    else :

        sm_avg[plat] = time

        count[plat] = 1

for k in sm_avg :

    sm_avg[k] = sm_avg[k] / count[k]

print("avg social media time :", sm_avg)



# 5 . highest negative interactions

max_neg = max([int(p.get("negative_interactions_count",0)) for p in data])

print("Highest negative interactions : ")

for p in data :

    if int(p.get("negative_interactions_count")) == max_neg :

        print(p.get("person_name"),end=",")

print()

# 6 . avg stress level by gender

stress_sum = {}

stress_count = {}

for p in data :

    g = p.get("gender")

    s = int(p.get("stress_level",0))

    if g in stress_sum :

        stress_sum[g] += s

        stress_count[g] += 1

    else :

        stress_sum[g] = s

        stress_count[g] = 1

g_avg = { g : stress_sum[g]/stress_count[g] for g in stress_sum }

print("avg stress level by gender :", g_avg)



# 7 . lowest mood users

min_mood = min([int(p.get("mood_level")) for p in data])

for p in data :

    if int(p.get("mood_level")) == min_mood :

        print((p.get("person_name"), p.get("platform")),end=",")

print("lowest mood :", min_mood)



# 8 . total positive interactions per platform

pos_total = {}

for p in data :

    plat = p.get("platform")

    val = int(p.get("positive_interactions_count",0))

    if plat in pos_total :

        pos_total[plat] += val

    else :

        pos_total[plat] = val

print("total positive interactions :", pos_total)



# 9 . physical activity > 45 minutes

high_act = [ p.get("person_name") for p in data if int(p.get("physical_activity_min",0)) > 45 ]

print("high physical activity users :", high_act,"Count : ",len(high_act))



# 10 . platform with highest avg anxiety level

anx_sum = {}

anx_count = {}

for p in data :

    plat = p.get("platform")

    a = int(p.get("anxiety_level",0))

    if plat in anx_sum :

        anx_sum[plat] += a

        anx_count[plat] += 1

    else :

        anx_sum[plat] = a

        anx_count[plat] = 1

avg_anx = { plat : round(anx_sum[plat]/anx_count[plat],2) for plat in anx_sum }

print("avg anxiety by platform :", avg_anx)
