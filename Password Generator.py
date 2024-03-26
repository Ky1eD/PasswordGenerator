import string
import random
print("Welcome to random password generator!")
# Get password length
length = int(input("Enter Password length: "))
# Get character types in password
print('''Chose the type of characters you wish to have in the password
    1. Digits
    2. Letters
    3. Special characters
    4. Uppercase 
    5. Done''')

characterList = ""

while True:
    choice = int(input("Pick a number: "))
    if(choice == 1):
        #adding letters
        characterList += string.ascii_letters
    elif(choice == 2):

        #adding digits
        characterList += string.digits
    elif (choice == 3):

        #adding special characters
        characterList += string.punctuation
    elif (choice == 4):

        #add uppercase letters
        characterList += string.ascii_uppercase
    elif (choice == 5):
        break

    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    #picking random character from our character list
    randomchar = random.choice(characterList)

    password.append(randomchar)

print("The Random password is" + "".join(password))







