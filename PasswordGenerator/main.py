#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
genPassword = []
for l in range(0, nr_letters):
    random_letters = random.randint(0, len(letters))
    genLetter = letters[random_letters - 1]
    genPassword.append(genLetter)
for n in range(0, nr_numbers):
    random_numbers = random.randint(0, len(numbers))
    genNumber = numbers[random_numbers - 1]
    genPassword.append(genNumber)
for s in range(0, nr_symbols):
    random_symbols = random.randint(0, len(symbols))
    genSymbol = symbols[random_symbols - 1]
    genPassword.append(genSymbol)
shuffle_password = genPassword
final_password = ''.join(genPassword)
print(final_password  + " : This is the password without shuffle:")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(shuffle_password)
shuffle_password = ''.join(shuffle_password)
print(shuffle_password + " : This is the password with all characters shuffled")