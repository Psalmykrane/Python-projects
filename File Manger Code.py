# Import libraries
import getpass as gp
import os 
import shutil
    
# PASSWORD CHECK FUNCTION
def plen(var):
    count = 0

    while True:
        var = input('Enter a password? ')
        if len(var) <=4:
            print(var)
            break
        else:
            print('Enter a four-digit password')


# Create an empty list for files
general_files=[]
hidden_files = []

# General file function
def gen_file():
    for i in os.listdir("Files"):
        i = i.strip()
        general_files.append(i)

# Hidden file function
def hid_file():
    for i in os.listdir("hidden"):
        i = i.strip()
        hidden_files.append(i)

# Welcome message
print("")
print("WELCOME! \n Setup Admin Password")

# Create password for Admin and check if password is correct
while True:
    adpin = gp.getpass("Enter Password: ")
    adpin2 = gp.getpass("Enter Password again: ")
    if adpin == adpin2:
        print("Password set successfully!")
        break
    else:
        print("Passwords do not match!")
print("")
print("Welcome, Admin!")
print("")

# Cfreate staff password and check if password is correct
print("Setup Staff Default Password")
print("")
    
while True:
    spin = gp.getpass("Enter Password: ")
    spin2 = gp.getpass("Enter Password again: ")
    if spin==spin2:
        print("Password set successfully!")
        break
    else:
        print("Passwords do not match!")
    print("")
    
# Begining of File management functions 

def testing():  
    print("")    
    print("Welcome Back!")
    
    # Password check before accessing files
    key1 = gp.getpass("Enter your password : ")
    file = os.listdir("Files")
    
    new_check = True
    s_check = True
    if key1==adpin:
        gen_file()
        print(general_files)
        print("")    

        hid_file()
        print(hidden_files)
        
        # Command options
        while new_check:   
            print("""Manage Files: \n 1. Move a file to Restricted Folder.\n 2. Restore a Hidden file \n 3. Open Files \n 4. Log Out""")
            w= input("Enter number: ")
            
            # To hide a file
            if w =="1":
                g = input("Enter filename to be hidden: ")
                if g in general_files:
                    shutil.move(f"./Files/{g}", f"./hidden/{g}")
                    hid_file()
                    gen_file()
                    print("File Hidden Successfully!")
                else:
                    print("File not Found!")
            
            # To restore an hidden file
            elif w == "2":
                h= input("Enter filename to be restored: ")
                if h in hidden_files:
                    shutil.move(f"./hidden/{h}", f"./Files/{h}")
                    hid_file()
                    gen_file()
                    print("File Restored Successfully!")
                    
            # To access general files
            elif w =="3":
                print(general_files)
                print(hidden_files)
                op_file=input("Enter file name: ")
                if op_file in general_files:
                    with open(f"./Files/{op_file}") as fil:
                        for i in fil:
                            print(i)
                elif op_file in hidden_files:
                    with open(f"./hidden/{op_file}") as fil:
                        for i in fil:
                            print(i)
                else:
                    print("File not Found")
                
            # Log out    
            elif w == "4":
                print("Logged Out successfully!")
                new_check = False

                testing()
                
                
            else:
                print("Invalid entry! Try again!")
        
        # To access a file
    elif key1 == spin:
        while s_check: 
            gen_file()
            print("Manage Files: \n 1. Open File  \n 2. Log Out")

            x  = input("Enter number: ")
            if x =="1":
                print(general_files)
                op_file=input("Enter file name: ")
                with open(f"./Files/{op_file}") as fil:
                    for i in fil:
                        print(i)

            elif x == "2":
                print("Logged out successfully")
                s_check = False
                testing()
            else:
                print("Passwords do not match!")
                testing()
    else:
        print("Incorrect Password!")
        testing()
    print("")
testing()