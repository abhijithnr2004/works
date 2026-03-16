from copy import deepcopy

arun_fvt_foods = [
    ["dosa","tea"],
    ["meals","lime juice"],
    ["chapathy","lime tea"]
]

resin_fvt_foods = deepcopy(arun_fvt_foods)

resin_fvt_foods[0][0] = "idly"

print("arun fvt food :",arun_fvt_foods)

print("Resin fvt food : ",resin_fvt_foods)