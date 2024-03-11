path_orig = r"C:\Users\ASUS\Desktop\PP2\lab6\7.txt"
file = open(path_orig, "r")
file = file.read()

file1 = open(r"C:\Users\ASUS\Desktop\PP2\lab6\7_1.txt", "w")

file1 = file1.write(file)
