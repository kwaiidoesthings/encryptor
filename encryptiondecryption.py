import random
import string

# creates list of every key, and creates key list that will be used to shuffle
detail = " " + string.punctuation + string.digits + string.ascii_letters
detail = list(detail)
key = detail.copy()

random.shuffle(key)

# function encrypts text 
def encryption():
    unencrypted_text = input("Enter a message to encrypt: ")
    cipher = ""

    for letter in unencrypted_text:
        index = detail.index(letter)
        cipher += key[index]

    print(f"original message : {unencrypted_text}")
    print(f"encrypted message: {cipher}")
    

# function decrypts text
def decrpytion():
    cipher = input("Enter a message to decrypt: ")
    unencrypted_text = ""

    for letter in cipher:
        index = key.index(letter)
        unencrypted_text += detail[index]

    print(f"encrypted message: {cipher}")
    print(f"original message : {unencrypted_text}")
    
# function sends start message and sends user to encrypt, decrypt, or quit 
def start():
    while True:
            dore = input("Would you like to Encrypt Message or Decrypt Message? (E/D/Q)")
            if dore == "E":
                encryption()
            elif dore == "D":
                decrpytion()
            elif dore == "Q":
                print("Goodbye!")
                return
            else:
                print("Please write E or D")

start()

