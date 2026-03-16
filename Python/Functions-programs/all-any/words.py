words = ["housefull","peaceful","program","beautiful","harmful","powerful","thinkful"]

is_ending_with_full = [ w.endswith("ful") for w in words]

is_all_ends_with_full = all(is_ending_with_full)

print("all ends with ful :",is_all_ends_with_full)

start_with_pro = [w.startswith("pro") for w in words]

is_any_start_with_pro = any(start_with_pro)

print("any start with pro :",is_any_start_with_pro)

