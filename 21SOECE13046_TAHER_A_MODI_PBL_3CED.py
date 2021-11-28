import os
import os.path
import shutil

x=0
while x !=1:
    origin_input = input("Enter Original Path Of Your Folder :- ")
    try:
        os.chdir(origin_input)
        x=1
    except:
        x=0
        print("Invalid Input Path ")

path = os.listdir()
x=0
while x!=1:
    destination_input = input("Destination Path Of Your Folder :- ")
    try:
        os.chdir(destination_input)
        x=1
    except:
        x=0
        print("Invalid Destination Path")

for i in path:
    
    if os.path.isfile(i):
        try:
            temp = i.index('.')
        except:
            pass
        folder_name  = i[temp+1:]
        if  not os.path.isdir(folder_name):
            os.mkdir(folder_name)
            try:
                shutil.move(f"{origin_input}/{i}",f"{destination_input}/{folder_name}")
            except:
                pass
        else:
            try:
                shutil.move(f"{origin_input}/{i}",f"{destination_input}/{folder_name}")
            except:
                pass