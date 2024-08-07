import enc,gapi,user,sys
usr,encr,googleAPI= user,enc,gapi
def m():
        while True:
            ifu = input("\n up - Uploading  , d - Download , l - Log Out , e - Exit\n").lower()
            if(ifu == "up"):
                while True:
                    print("\n Make sure the file in the 'F' folder are the ones you want to upload.To return to the main menu, type return.\n")
                    ifu = input("put file here: ")
                    if(ifu == "return"):
                        break
                    else:
                       encr.e(ifu, encr.rk())
                       googleAPI.uf(ifu)

            elif(ifu == "e"):
                print("Exit")
                sys.e()

            elif(ifu == "l"):
                print("Log out")
                break

            elif(ifu == "d"):
                while True:
                    ifu = input("\n search - Searching , d - downloading  ,e - Exit\n").lower()
                    if(ifu == "s"):
                        ifu = input("put file here: ")
                        googleAPI.sfl(ifu)
                    elif(ifu == "d"):
                        ifu = input("put file here: ")
                        fileID= googleAPI.fid1(ifu)
                        googleAPI.df(fileID, ifu)
                        encr.d(ifu, encr.rk())
                    elif(ifu == "e"):
                        break
                    else:
                        print("Incorrect")
            else:
                 print("Incorrect")

def sm():
        while True:
            uin = input("\n up - Uploading  , d - Download ,usersettings -For User Setting, l - Log Out , e - Exit\n").lower()
            if(uin == "usersettings"):
                while True:
                    uin = input("\n add - Add User , d - Delete User , e - Exit\n").lower()
                    if (uin == "add"):
                        usr.au()
                    elif(uin == "d"):
                        usr.du()
                    elif(uin == "e"):
                        break
                    else:
                        print("Incorrect")

            elif(uin == "up"):
                while True:
                    print("\nMake sure the file in the 'F' folder are the ones you want to upload.To return to the main menu, type return.\n")
                    uin = input("put file here: ")
                    if(uin == "return"):
                        break
                    else:
                       encr.e(uin, encr.rk())
                       googleAPI.uf(uin)

            elif(uin == "e"):
                print("Exit")
                sys.e()
            elif(uin == "l"):
                usr.flg = False
                print("Log out")
                break
            elif(uin == "d"):
                while True:
                    uin = input("\n search - Searching , d - Downloading , e - Exit\n").lower()
                    if(uin == "s"):
                        uin = input("put file here: ")
                        googleAPI.sfl(uin)
                    elif(uin == "d"):
                        uin = input("put file here: ")
                        fileID= googleAPI.fileID(uin)
                        googleAPI.df(fileID, uin)
                        encr.d(uin, encr.keyRead())
                    elif(uin == "e"):
                        break
                    else:
                        print("Incorrect")
            else:
                 print("Incorrect")