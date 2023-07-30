# take the input as text
text = input("Enter the string to convert into the hidden msg : ")

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shift=int(input("Enter the value of the shift amount : "))


def encrypt(text, shift):
    encryptext=""
    for letter in text:
        pos=alpha.index(letter)
        pos=(pos+shift)%26
        encryptext+=alpha[pos]
    print("Encrypting")
    print(encryptext)
    print("decrypting")
    decrypt(encryptext,shift)
print(text)

def decrypt(text,shift):
    decryptext=""
    for letter in text:
        pos=alpha.index(letter)
        pos=pos-shift
        if pos<0:
            pos+=26
            decryptext+=alpha[pos]
        else:
            decryptext+=alpha[pos]
    print(decryptext)
encrypt(text,shift)