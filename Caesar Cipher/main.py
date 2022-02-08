PINK = '\033[95m'
ENDC = '\033[0m'

lower_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

final = ''

def encrypt(text: str, shift: int):
    global final

    for letter in text:
        if letter in lower_alphabet:
            final += lower_alphabet[(lower_alphabet.index(letter) + shift) % len(lower_alphabet)]
        elif letter in upper_alphabet:
            final += upper_alphabet[(upper_alphabet.index(letter) + shift) % len(upper_alphabet)]
        else:
            final += letter

    print("ENCRYPTED TEXT:")
    print(PINK + final + ENDC)

def decrypt(text: str):
    global final

    knows_shift = input(f"Do you know the shift? {PINK}y/n{ENDC}\n")

    if knows_shift == "y":
        shift = int(input(f"What is the letter shift? {PINK}(0-25){ENDC}\n"))

        for letter in text:
            if letter in lower_alphabet:
                final += lower_alphabet[(lower_alphabet.index(letter) - shift) % len(lower_alphabet)]
            elif letter in upper_alphabet:
                final += upper_alphabet[(upper_alphabet.index(letter) - shift) % len(upper_alphabet)]
            else:
                final += letter

        print("DECRYPTED TEXT:")
        print(PINK + final + ENDC)

    else:
        print("DECRYPTED TEXTS:\n")
        for i in range(26):
            final = ''
            for letter in text:
                if letter in lower_alphabet:
                    final += lower_alphabet[(lower_alphabet.index(letter) + i) % len(lower_alphabet)]
                elif letter in upper_alphabet:
                    final += upper_alphabet[(upper_alphabet.index(letter) + i) % len(upper_alphabet)]
                else:
                    final += letter
            print(PINK + final + ENDC)

def main():

    print("""
       _       _               
      (_)     | |              
   ___ _ _ __ | |__   ___ _ __ 
  / __| | '_ \| '_ \ / _ \ '__|
 | (__| | |_) | | | |  __/ |   
  \___|_| .__/|_| |_|\___|_|   
        | |                    
        |_|         
""")

    option = input(f"Would you like to encrypt, or decrypt a message?{PINK} (encrypt/decrypt) {ENDC}\n")

    if option == "encrypt" or option == "e":
        cipher = input("Input the text you would like to encrypt:\n")
        shift = int(input(f"How many letters do you want to shift the message by? {PINK}(0-25){ENDC}\n"))
        encrypt(cipher, shift)
        return main()
    elif option == "decrypt" or option == "d":
        cipher = input("Input the text you would like to decrypt:\n")
        decrypt(cipher)
        return main()
    else:
        print("Please choose to encrypt or decrypt.")
        return main()

main()