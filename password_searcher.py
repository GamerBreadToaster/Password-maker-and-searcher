import os

def password_searcher():
    file_is = False
    found = False
    path = "passwords.txt"
    found_passwords = ""
    if os.path.isfile(path):
        print("there is an passwords.txt file")
        file_is = True
    else:
        print("go make an password with the password_maker.py")
    while file_is == True:
        with open(path, "r") as file:
            tried = file.readlines()
        
        tag = input("fow what tag do you want to search or password?: ")
        i = len(tried)
        for b in range(1,i):
            password = tried[b]
            if tag in password:
                found_passwords += password
        if found_passwords != "":
            path = "found_passwords.txt"
            with open(path, "w") as file:
                file.write("found passwords:\n")
                for a in range(len(found_passwords)):
                    with open(path, "a") as file:
                        file.write(found_passwords[a])
            print("The found passwords are in found_passwords.txt")
            print("it took", b, "tries")
        elif found_passwords == "":
            print("no passwords found")
        break
    os.system('pause')
