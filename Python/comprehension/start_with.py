words = ["profession","cat","act","program","dam","process"]

start_with_pro = { w for w in words if w.startswith("pro") }

print("words starting wth pro : ",start_with_pro)

ends_with_am = { w for w in words if w.endswith("am") }

print("words ending with am : ",ends_with_am)

