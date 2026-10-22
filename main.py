# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ").strip()
if name == "":
    print("Name is required.")
try:
    previous = float(input("Enter previous meter reading: "))
    if 0 <= previous:
        print("Integer Accepted")
    
    else:
        print("Use a number that is at least 0")
    
except ValueError:
    print("Enter a valid integer")

current = float(input("Enter current meter reading: "))
try:
    if previous <= current:
        print("Integer accepted")
    
    else:
        print("Use a number atleast the previous reading")
    
except ValueError:
    print("Enter a valid integer")
    

    

consumption = current - previous
total_bill = consumption * RATE


print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))


    

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading