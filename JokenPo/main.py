import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
jokenpo = [scissors, paper, rock]
computer_select = random.randint(0, len(jokenpo))
computer_choice = jokenpo[computer_select]

player_choice = input('Please select: "Paper" "Scissors" "Rock" : ').lower()
if player_choice == "rock":
    print(rock)
    player_choice = jokenpo[2]
elif player_choice == "paper":
    print(paper)
    player_choice = jokenpo[1]
elif player_choice == "scissors":
    print(scissors)
    player_choice = jokenpo[0]
print(f"Computer chose:\n{computer_choice}")
if player_choice == paper and computer_choice == paper:
    print("Tie")
elif player_choice == paper and computer_choice == rock:
    print("You Win")
elif player_choice == paper and computer_choice == scissors:
    print("You Lose")
if player_choice == scissors and computer_choice == scissors:
    print("Tie")
elif player_choice == scissors and computer_choice == paper:
    print("You Win")
elif player_choice == scissors and computer_choice == rock:
    print("You Lose")
if player_choice == rock and computer_choice == rock:
    print("Tie")
elif player_choice == rock and computer_choice == scissors:
    print("You Win")
elif player_choice == rock and computer_choice == paper:
    print("You Lose")