alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
input_text = input("Type your message:\n").lower()
shift_Number = int(input("Type the shift number:\n"))

def encryption(text,shift):
    str_encrypted= ""
    for letter in text:
        current_posn= alphabet.index(letter)
        new_posn=current_posn+shift
        str_encrypted+=alphabet[new_posn]
    print(str_encrypted)

def decryption(text,shift):
    str_decrypted=""
    for letter in text:
        posn=alphabet.index(letter)
        new_posn=posn-shift
        str_decrypted+=alphabet[new_posn]
    print(str_decrypted)
    
if (direction == 'encode'):
    encryption(text=input_text,shift=shift_Number)
else:
    decryption(text=input_text,shift=shift_Number)