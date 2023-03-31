import os
import random
import string

def password_maker():
    num_passwords = 1
    path = "passwords.txt"
    password_length = 4
    tags = "empty"
    randommise = True
    if os.path.isfile(path):
        print("there is an passwords.txt file")
    else:
        with open(path, "w") as file:
            file.write("//welcome to your passwords!\\\\\n")
    
    def generate_password(length, strength):
        letters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(letters) for i in range(length))
        return password
    while True:
        os.system('cls')
        print("options:")
        print("type the number to change them")
        print(f"1: Length password: {password_length}")
        print(f"2: amount passwords: {num_passwords}")
        print(f"3: tags: {tags}")
        print(f"4: randomise the password: {randommise}")
        print("5: save and exit")
        choose = int(input("choose here: "))
        if choose == 1:
            password_length = int(input("The password length: "))
        if choose == 2:
            num_passwords = int(input("The amouth of passwords: "))
        if choose == 3:
            tags = input("The tag(s) of passwords: ")
        if choose == 4:
            randommise = int(input("randommise? 0 for no, 1 for yes: "))
            if randommise == 0:
                randommise = False
            elif randommise == 1:
                randommise = True
        if choose == 5:
            break
    
    num_passwords = int(input("How many passwords do you want to generate?: "))
    password_length = int(input("How long do you want the passwords to be?: "))
    tag = input("what tag(s) does your password have? ")
    randommise = int(input("Do you want to randomise you password? 1 True, 2 False: "))
    
    for i in range(num_passwords):
        if randommise == 1:
            password = generate_password(password_length)
        elif randommise == 2:
            password = input("input you password here then: ")
        with open(path, "a") as file:
            file.write(F"tags: {tag}: {password}\n")
        print(password)
