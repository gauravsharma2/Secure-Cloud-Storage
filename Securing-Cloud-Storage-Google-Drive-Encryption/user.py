import pickle
import getpass

def lda(ur):
    try:
        with open('Usr/' + ur + '.pkl', 'rb') as f:
          return pickle.load(f)
    except Exception:
          pass

ur = lda("list")

flg = False
if not ur:
    acc = 0
else:
    acc = 1

def slt(o, ur ):
    with open('Usr/'+ ur + '.pkl', 'wb') as f:
        pickle.dump(o, f, pickle.HIGHEST_PROTOCOL)

def au():   
    while True:
        uint = input("enter user:")
        if uint in ur:
            print("present")
        else:
            pass_ = getpass.getpass("enter password:")
            ur[uint] = pass_
            slt(ur, "list")
            print(" created")
            break

def du():
    unm = input("write user to delete:")
    if unm == "admin":
        print("not able to delete")
    elif unm in ur:
        del ur[unm]
        slt(ur, "list")
        print("deleted")
        
def login():
    global flg
    cnt = 0
    while True:
        _input = input("write")
        _pass = getpass.getpass("type pass :")
        if _input in ur and ur[_input] == _pass and _input == "admin":
            flg = True
            print("Logged in")
            break
        elif _input in ur and ur[_input] == _pass:
            print("Logged in")
            break
        else:
            cnt = cnt+1
            
