cart1 = {"Milk", "Bread", "Eggs", "Butter"}
cart2 = {"Bread", "Juice", "Eggs", "Cheese"}

common_items = cart1.intersection(cart2)

only_by_customer_1 = cart1.difference(cart2)

only_by_customer_2 = cart2.difference(cart1)

bought_atleast_one_customer = cart1.symmetric_difference(cart2)

print(f"Items both customers bought {common_items}")

print(f"Items bought only by Customer 1 {only_by_customer_1}")

print(f"Items bought only by Customer 2 {only_by_customer_2}")

print(f"Items bought by at least one customer {bought_atleast_one_customer}")


