for year in range(1800,2026) :

    if year%4 == 0 and ( year%400 == 0 or year%100 != 0) :
        print(year)