item1 = 60.0
item2 = 70.0
item3 = 90.0

total_budget = 160.0

cost = 0.0
cost = item1 + item2 + item3

print("The total cost = ", cost, "$")

if cost <= total_budget:
    print("You are within the budget.")
    print("Money left = ", total_budget - cost, "$")
else:
    print("You are over budget.")
    print("Additional money needed = ", cost - total_budget, "$")
