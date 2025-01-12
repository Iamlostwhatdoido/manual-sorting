import os

def compare2(a,b):
    answer = 0
    while answer != 1 and answer !=2:
        os.system('cls')
        print("[1] ",a)
        print("[2] ",b)
        print("\nYour best : ")
        try:
            answer = int(input())
        except:
            pass
        os.system('cls')
    
    if answer == 1:
        return a
    else:
        return b