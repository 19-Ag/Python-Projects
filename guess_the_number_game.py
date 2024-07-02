import random
logo="""
  ____  __ __    ___  _____ _____     ______  __ __    ___      ____   __ __  ___ ___  ____     ___  ____  
 /    ||  |  |  /  _]/ ___// ___/    |      ||  |  |  /  _]    |    \ |  |  ||   |   ||    \   /  _]|    \ 
|   __||  |  | /  [_(   \_(   \_     |      ||  |  | /  [_     |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||    _]\__  |\__  |    |_|  |_||  _  ||    _]    |  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     ||     ||     |\    |\    |      |  |  |  |  ||     |    |  |  ||     ||   |   ||     ||     ||  .  \
|___,_| \__,_||_____| \___| \___|      |__|  |__|__||_____|    |__|__| \__,_||___|___||_____||_____||__|\_|
                                                                                                           
"""
print(logo)
def difficulty_choice(choice):
    """Asks the user to choose a difficulty level for the game."""
    if choice == "easy":
        print("You chose easy! The game will be easy to play.")
        tries=10
    elif choice=="hard":
        print("You chose hard! The game will be challenging.")
        tries=5
    return tries
def game():
    """The game function. It asks the user to guess a number between 1 and 100"""
    choice=input("Enter the difficulty level 'easy' or 'hard' ").lower()
    tries=difficulty_choice(choice)
    print("You have",tries,"tries to guess the number.")
    number=random.randint(1,100)
    while tries>0:
        guess=int(input("Enter your guess: "))
        if guess<number:
            print("The guess is too low ")
            print(f"guesses remaining={tries-1}")
        elif guess>number:
            print("The guess is too high ")
            print(f"guesses remaining={tries-1}")
        else:
            print("You guessed the number! You win!")
            break
        tries-=1
    if tries==0:
        print("You weren't able to guess the number ")
game()   
    
