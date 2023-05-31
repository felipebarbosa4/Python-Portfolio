
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
small = 15
medium = 20
large = 25
pepperoni_small = 2
pepperoni_medium_large = 3
more_cheese = 1
if size == "S":
    bill += small
    if add_pepperoni == "Y":
        bill += pepperoni_small
    if extra_cheese == "Y":
        bill += more_cheese

if size == "M":
    bill += medium
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large
    if extra_cheese == "Y":
        bill += more_cheese

if size == "L":
    bill += large
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large
    if extra_cheese == "Y":
        bill += more_cheese

print(f"your final bill is: ${bill}")