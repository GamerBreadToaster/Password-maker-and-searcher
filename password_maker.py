import os
import random
import string, time

def password_maker():
    num_passwords = 1
    path = "passwords.txt"
    password_length = 4
    tags = "empty"
    randommise = True
    username = "example@mail.com"
    password = "examplePassword"
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
        print(f"""options:
type the number to change them
1: Length password: {password_length}
2: amount passwords: {num_passwords}
3: tags: {tags}
4: username: {username}
5: randomise the password: {randommise}""")
        if randommise == False:
            print(f"6: password: {password}")
        print("7: save and exit")
        choose = int(input("choose here: "))
        if choose == 1:
            password_length = int(input("The password length: "))
        if choose == 2:
            num_passwords = int(input("The amouth of passwords: "))
        if choose == 3:
            tags = input("The tag(s) of passwords: ")
        if choose == 4:
            username = input("enter the username or email for the password: ")
        while choose == 5:
            if randommise == True:
                randommise = False
                break
            if randommise == False:
                randommise = True
                break
        if choose == 7:
            break
    time_begin = time.time()
    for i in range(num_passwords):
        if randommise == 1:
            password = generate_password(password_length,1)
        elif randommise == 2:
            password = input("input you password here then: ")
        with open(path, "a") as file:
            file.write(F"tags: {tags} | username: {username} | password: {password}\n")
    time_end = time.time()
    print("it took", (time_end - time_begin), "seconds")
    os.system('pause')
