alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

option = input("Do you wish to encode or decode the message? ").lower()
shift = int(input("Enter the shift amount: "))
message = input("Enter the message: ")
new_message = ""

if option == "encode":
    for char in message:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (idx + shift) % len(alphabet)
            new_char = alphabet[new_idx]
            new_message += new_char
        else:
            new_message += char  # Keep non-alphabet characters unchanged
    print("Encoded message:", new_message)
elif option=="decode":
    for char in message:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (idx - shift) % len(alphabet)
            new_char = alphabet[new_idx]
            new_message += new_char
        else:
            new_message += char  # Keep non-alphabet characters unchanged
    print("Decoded message:", new_message)