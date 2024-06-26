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

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")

if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
elif choice == "2":
    print(scissors)

computer_choice = random.randint(0, 2)  # Generate random integer between 0 and 2 inclusive

if computer_choice == 0:
    print("Computer chose: \n" + rock)
elif computer_choice == 1:
    print("Computer chose: \n" + paper)
elif computer_choice == 2:
    print("Computer chose: \n" + scissors)

# Convert choice to integer for comparison
choice = int(choice)

# Determine the winner
if (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
    print("You lose!")
elif choice == computer_choice:
    print("Draw!")
else:
    print("You win")
