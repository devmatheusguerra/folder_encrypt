import sys
import os
from os import system as exec
from hashlib import sha256
from time import sleep as wait
from getpass import getpass
from src.Encrypt import Encrypt
from src.Finder import Finder
CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"
OPEN_COMMAND = "start" if os.name == "nt" else "open"

print('''
==============================================================================================================
==============================================================================================================
==============================================================================================================
 __    __     _                            _            ___     _     _            ___     _       _   
/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___     / __\__ | | __| | ___ _ __ / __\ __(_)_ __ | |_ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   / _\/ _ \| |/ _` |/ _ \ '__/ / | '__| | '_ \| __|
 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | / / | (_) | | (_| |  __/ | / /__| |  | | |_) | |_ 
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \/   \___/|_|\__,_|\___|_| \____/_|  |_| .__/ \__|
                                                                                            |_|        
==============================================================================================================
==============================================================================================================
==============================================================================================================
''')
      
wait(2)
exec(CLEAR_COMMAND)

if (os.path.isfile('system.key')):
    with open('system.key', 'rb') as f:
        SYSTEM_KEY = f.read()
else:
    print("Generating system key...")
    with open('system.key', 'wb') as f:
        SYSTEM_KEY = sha256(os.urandom(32)).hexdigest()
        f.write(SYSTEM_KEY.encode())
    wait(2)
    exec(CLEAR_COMMAND)

if (os.path.isfile('user.key')):
    USER_KEY = getpass("Enter your key: ")
    print("Verifying key...")
    wait(2)
    exec(CLEAR_COMMAND)
    if sha256(USER_KEY.encode()).hexdigest() != open('user.key', 'rb').read().decode():
        print("Invalid key!")
        sys.exit()
    else:
        while True:
            try:
                option = int(input('''
Choose an option:
1. Encrypt a folder
2. Decrypt a folder
3. Exit
Type the number of the option: '''))
                if option == 1 or option == 2:
                    folder_path = Finder().find()
                else:
                    folder_path = None
                
                if (option == 1):
                    Encrypt().encrypt(folder_path)
                    print(f"Encrypting {folder_path}...")
                    wait(1)
                elif (option == 2):
                    Encrypt().decrypt(folder_path)
                    print(f"Decrypting {folder_path}...")
                    wait(1)
                elif (option == 3):
                    print("Bye!")
                    wait(1)
                    sys.exit()

                exec(CLEAR_COMMAND)
                print("Done!")
                wait(1)
                exec(OPEN_COMMAND + " " + folder_path)
            except ValueError:
                if (folder_path == None):
                    print("Invalid path!")
                else:
                    print("Invalid option!")

else:
    # If not user key, generate one
    with open('user.key', 'wb') as f:
        while True:
            pwd1 = getpass("Type a password: ")
            pwd2 = getpass("Confirm the password: ")
            if pwd1 == pwd2:
                break
            else:
                exec(CLEAR_COMMAND)
                print("Passwords don't match!")
                wait(2)
                exec(CLEAR_COMMAND)

        USER_KEY = sha256(pwd1.encode()).hexdigest()
        f.write(USER_KEY.encode())
        print("Key saved! Rerun the program to continue.")
        sys.exit()
    
        
