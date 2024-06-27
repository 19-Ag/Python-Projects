import random
import string

print("Welcome to the password generator")

letters_input = int(input("How many letters would you like in your password? "))
symbols_input = int(input("How many symbols would you like in your password? "))
numbers_input = int(input("How many numbers would you like in your password? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

for i in range(letters_input):
    password.append(random.choice(letters))

for j in range(numbers_input):
    password.append(random.choice(numbers))

for k in range(symbols_input):
    password.append(random.choice(symbols))

# Shuffle the password to mix characters, numbers, and symbols
random.shuffle(password)

# Join the list into a single string
password_str = ''.join(password)

print("Generated password:", password_str)
