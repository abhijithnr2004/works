vehicles = [
    {"name": "Swift", "brand": "Maruti Suzuki", "price": 650000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Baleno", "brand": "Maruti Suzuki", "price": 820000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Creta", "brand": "Hyundai", "price": 1500000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "i20", "brand": "Hyundai", "price": 950000, "model": 2021, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Seltos", "brand": "Kia", "price": 1600000, "model": 2023, "color": "Silver", "fuel_type": "Diesel"},
    {"name": "Sonet", "brand": "Kia", "price": 1200000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Harrier", "brand": "Tata", "price": 1900000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "Nexon", "brand": "Tata", "price": 1200000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Punch", "brand": "Tata", "price": 800000, "model": 2023, "color": "Green", "fuel_type": "Petrol"},
    {"name": "XUV700", "brand": "Mahindra", "price": 2200000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Thar", "brand": "Mahindra", "price": 1700000, "model": 2022, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Scorpio N", "brand": "Mahindra", "price": 2000000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "City", "brand": "Honda", "price": 1500000, "model": 2021, "color": "Silver", "fuel_type": "Petrol"},
    {"name": "Amaze", "brand": "Honda", "price": 900000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Kiger", "brand": "Renault", "price": 800000, "model": 2021, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Duster", "brand": "Renault", "price": 1300000, "model": 2020, "color": "Brown", "fuel_type": "Diesel"},
    {"name": "EcoSport", "brand": "Ford", "price": 1100000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Endeavour", "brand": "Ford", "price": 3600000, "model": 2020, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Altroz", "brand": "Tata", "price": 950000, "model": 2022, "color": "Golden", "fuel_type": "Petrol"},
    {"name": "Venue", "brand": "Hyundai", "price": 1300000, "model": 2023, "color": "Red", "fuel_type": "Petrol"}
]

# all_brands = { v.get("brand") for v in vehicles }

# print(all_brands)

# display vehcle names whose color = red

red_vehicles = [ v["name"] for v in vehicles if v["color"]=="Red" ]

print("Red colour vehicles : ",red_vehicles)

# display vehicles names  whose model 2022

vehicle_2022 = [ v["name"] for v in vehicles if v["model"]==2022 ]
print("2022 model vehicles : ",vehicle_2022)

# display diesel vehile names

diesel_vehicle = [ v["name"] for v in vehicles if v["fuel_type"]=="Diesel" ]
print("Diesel vehicles : ",diesel_vehicle)

# display all vehicle price

all_vehicle_price = { v.get("name") : v.get("price")  for v in vehicles }
print("price of all Vehicles : ",all_vehicle_price)

# display vehicle names whose price > 10lac

greater_than_10lakh = [ v["name"] for v in vehicles if v["price"]>1000000 ]
print("Vehicles with price greater than 10 lakh : ",greater_than_10lakh)

# display tata vehicle names

tata_vehicles = [ v["name"] for v in vehicles if v["brand"]=="Tata" ]
print("tata vehicles : ",tata_vehicles)

# display tata vehicle whose model 2022

tata_vehicles_2022 = [ v["name"] for v in vehicles if v["brand"]=="Tata" and v["model"]==2022 ]
print("2022 model tata vehicles : ",tata_vehicles_2022)

# display vehcle availabe at lowest price

lowest_price_vehicle = [v["name"] for v in vehicles if v["price"] == min(v["price"] for v in vehicles)]
print("lowest price vehicle : ",lowest_price_vehicle)

# dsipaly prices of maruthi suzuki vehicles

maruthi_vehicles_price = { v.get("name") : v.get("price")  for v in vehicles if v.get("brand")=="Maruti Suzuki" }
print("Maruthi suzuki vehicles : ",maruthi_vehicles_price)

# display hundayi vehicle names avaiale at > 5lac

hyundai_vehicles_gt_5lakh = [ v["name"] for v in vehicles if v["brand"]=="Hyundai" and v["price"] > 500000 ]
print("Hyundai vehicles with price greater than 5 lakh : ",hyundai_vehicles_gt_5lakh)

# display vehicle names whose model in range of 2022 - 2024

vehicles_2022_to_2024 = [ v["name"] for v in vehicles if v["model"] in range(2022,2025) ]
print("vehicles with model in range 2022 - 2024 : ",vehicles_2022_to_2024)


