def bmi(height_in_cm,weight_in_kg) :

    height_in_meter = height_in_cm/100
    
    return round(weight_in_kg/(height_in_meter**2))

print(bmi(179,72))