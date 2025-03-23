from pathlib import Path
import os
import shutil

def createfolder():
    name=input("Name your Folder:-")
    p=Path(name) 
    p.mkdir()
    print("Successfully Created the folder...")
    

def readfolder():
    path = Path("")
    items=list(path.rglob("*"))    # Recursive global.....
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")


def updatefolder():
    readfolder()
    old=input("Tell the name of the folder you want to update.")
    old_p=Path(old)
    if old_p.exists() and old_p.is_dir():
        new_name=input("tell your folder new name:-")
        new_p=Path(new_name)
        if not new_p.exists():
            old_p.rename(new_p)
        else:
            print("This folder is already exist")


def removefolder():
    readfolder()
    name=input("Name your Folder:-")
    p=Path(name) 
    if p.exists() and p.is_dir():
        shutil.rmtree()
        # p.rmdir()
        print("Successfully Deleted the folder...")
    else:
        print("No Such folder exists")


def createfile():
    name=input("Tell your filename:-")
    p=Path(name)
    if not p.exists():
        with open(p,"w") as f:
            data=input("What you want to write:-")
            f.write(data)
        print("file is created succesfully")
    else:
        print("file is already exists....")

def readfile():
    name=input("please tell your filename:-")
    p=Path(name)
    if p.exists() and p.is_file():
        with open(p,"r") as f:
            print(f.read())

        print("Read successfully.")
    else:
        print("No such file exist.")


def updatefile():
    readfolder()
    name=input("Tell your filename who want to Update:-")
    p=Path(name)
    if p.exists() and p.is_file():
        print("Press 1 for remaining the file.")
        print("Press 2 for overwriting the file.")
        print("Press 3 for appending content in file.")
        c=int(input("tell you response:-"))
        if c == "1":
            new_name=input("tell your file new name")
            new_path=Path(new_name)
            if new_path.exists():
                print("Sorry this file already exist")
            else:
                p.rename(new_path)

        if c == "2":
            with open(p,"w") as fs:
                fs.write(input("tell what you want to write:-"))
            print("Overwrited successfully")

        if c == "3":
            with open(p,"a") as fs:
                fs.write(" "+input("tell what you want to write:-"))
            print("Appended successfully")



def deletefile():
    name=input("please tell your filename:-")
    p=Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        print("File is successfully deleted..")
    else:
        print("no such file exists" )



print("Press 1 For creating a folder.")
print("Press 2 for raeding a folder.")
print("Press 3 for updating a folder.")
print("Press 4 for deleting a folder.")
print("Press 5 for creating a file.")
print("Press 6 for Reading a file.")
print("Press 7 for updating a file.")
print("Press 8 for deleting a file.")

check = input("Give your Response:-")

if check == "1":
    createfolder()

elif check == "2":
    readfolder()

elif check == "3":
    updatefolder()

elif check == "4":
    removefolder()

elif check == "5":
    createfile()

elif check == "6":
    readfile()

elif check == "7":
    updatefile()

elif check == "8":
    deletefile()