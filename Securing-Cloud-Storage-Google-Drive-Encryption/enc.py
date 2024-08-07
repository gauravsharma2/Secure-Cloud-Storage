from cryptography.fernet import Fernet

def kg():
    ky = Fernet.generate_key()
    f = open('k/ky.ky', 'wb')
    f.write(ky)
    f.close()

def rk():
    try:
        f = open('k/ky.ky', 'rb')
        ky = f.read()
        f.close()
        return ky
    except Exception:
        kg()
        rk()

def d(f_Name, Key):
    with open("download/"+ f_Name, "rb") as f:
        i = f.read()
    fernet = Fernet(Key)
    dm = fernet.decrypt(i)
    with open("download/"+ f_Name, "wb") as f:
        f.write(dm)

def e(f_Name, Key):
    with open("F/"+ f_Name, "rb") as f:
        i = f.read()
    fernet = Fernet(Key)
    em = fernet.encrypt(i)
    with open("F/"+ f_Name, "wb") as f:
        f.write(em)

