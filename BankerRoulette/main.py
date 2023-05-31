import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_integer = random.randint(0, len(names))
roulette = names[random_integer]
print(f"{roulette} is going to buy the meal today!")
