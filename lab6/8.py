import os

path_1 = r"C:\Users\ASUS\Desktop\PP2\lab6\folder\8.txt"

if os.path.exists(path_1) == True:
    os.remove(path_1)

else:
    print("Path doesn't exist")