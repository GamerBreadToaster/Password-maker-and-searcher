import os

def password_searcher():
    file_is = False
    found = False
    path = "passwords.txt"
    if os.path.isfile(path):
        print("there is an passwords.txt file")
        file_is = True
    else:
        print("go make an password with the password_maker.py")
    while file_is == True:
        with open(path, "r") as file:
            tried = file.readlines()
        
        tag = input("fow what tag do you want to search or password?: ")
        while found == False:
            i = 0
            while True:
                i += 1
                a = tried[i]
                if tag in a:
                    found = True
                    break
        print("password: ",a)
        print("it took", i, "tries")
        break
    os.system('pause')