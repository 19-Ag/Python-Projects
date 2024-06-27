import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)

while "_" in display:
    guess = input("Enter a letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(" ".join(display))

print("Congratulations, you won!")