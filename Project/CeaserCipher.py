plainText = input("Enter the text: ")
key = int(input("Enter the key: "))

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipherText = ''

for char in plainText:
    if char.isalpha():  # Check if the character is alphabetic
        # Determine if it's uppercase or lowercase
        is_upper = char.isupper()
        char_index = (values.index(char.lower()) + key) % 26
        encrypted_char = values[char_index]
        cipherText += encrypted_char.upper() if is_upper else encrypted_char
    else:
        cipherText += char  # Non-alphabetic characters remain unchanged

print("Cipher text:", cipherText)
