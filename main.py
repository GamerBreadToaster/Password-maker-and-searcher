import os
from password_maker import password_maker
from password_searcher import password_searcher

while True:
    os.system("cls")
    print("what do you want to do?:")
    print("1: make an password")
    print("2: search for an password")
    choose = int(input("choose here: "))
    if choose == 1:
        password_maker()
    if (choose) == 2:
        password_searcher()