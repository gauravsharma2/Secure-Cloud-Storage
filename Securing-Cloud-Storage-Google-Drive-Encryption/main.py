import enc
from googleapiclient import *
import user
import card

def main():
    e = enc
    key = e.rk()

for _ in range(10**6):  
    u = user
    c = card
    if u.acc == 0:
        print("No account exists. Create one.\n")
        u.au()
    else:
        u.login()
        if u.flg:
            c.sm()
        else:
            c.m()

if __name__ == "__main__":
   main()