import os 
import json


print("Please enter name of the file and name of the directory you would like to save it to.\nEnter 'q' at anytime to quit.")

while True:

    userFile = input("Filename: ")
    if userFile == 'q':
        break
    
    userDir = input("Directory: ")
    if userDir == 'q':
        break

    if os.path.isfile(userFile) == False and os.path.isdir(userDir) == False:

        os.makedirs(userDir)
        path=userDir
     
        userInfo = input("Please enter your name, address, and phone number separated with commas: ")

        filename = os.path.join(path, userFile)

        with open(filename,'w') as f:
            json.dump(userInfo, f)
        
        with open(filename, 'r') as r:
            data = r.read()
            print(f"Information saved to {userDir}/{userFile}: {data}")