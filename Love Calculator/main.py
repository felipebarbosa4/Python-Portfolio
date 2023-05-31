
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_name2 = str(name1) + str(name2)
match_true = 0
match_love = 0
lower_case_name1_name2 = name1_name2.lower()
if lower_case_name1_name2.count("t") > 0:
    match_true += lower_case_name1_name2.count("t")
if lower_case_name1_name2.count("r") > 0:
    match_true += lower_case_name1_name2.count("r")
if lower_case_name1_name2.count("u") > 0:
    match_true += lower_case_name1_name2.count("u")
if lower_case_name1_name2.count("e") > 0:
    match_true += lower_case_name1_name2.count("e")
if lower_case_name1_name2.count("l") > 0:
    match_love += lower_case_name1_name2.count("l")
if lower_case_name1_name2.count("o") > 0:
    match_love += lower_case_name1_name2.count("o")
if lower_case_name1_name2.count("v") > 0:
    match_love += lower_case_name1_name2.count("v")
if lower_case_name1_name2.count("e") > 0:
    match_love += lower_case_name1_name2.count("e")
match_true_love = str(match_true) + str(match_love)
match_true_love = int(match_true_love)

if match_true_love < 10 or match_true_love > 90:
    print(f"Your score is {match_true_love}, you go together like coke and mentos.")
elif 40 < match_true_love < 50:
    print(f"Your score is {match_true_love}, you are alright together.")
else :
    print(f"Your score is {match_true_love}.")