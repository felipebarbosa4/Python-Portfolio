import random

# import display as display

word_list = ["luna", "apollo", "brenda", "felipe", "mizifi", "edma", "augusto", "cecilia", "eunice", "joaozinho"]

random_word = random.randint(0, len(word_list))
chosen_word = word_list[random_word - 1]

underscores = "_" * (len(chosen_word))
split_underscores = list(underscores)

split_chosen_word = list(chosen_word)

print(split_underscores)
print("")

while split_underscores != split_chosen_word:
    guess = input("Chose a Letter : ").lower()
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            split_underscores[i] = letter
    print(split_underscores)

result_word = ''.join(split_underscores)
result_word_upper = result_word.upper()

print("")
print("CONGRATULATIONS !!!!")
print("")
print(f"The final word is {result_word_upper}!")
