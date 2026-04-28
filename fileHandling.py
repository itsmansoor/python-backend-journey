import os

#1. read file 
file = open('demo.txt','r')
print(file.read())
file.close()

#2. Write in File
f1 = open('demo2.txt','w')
f1.write('Hello Mansoor')
f1.close()

#3. Append in File

file = open("demo.txt", "a")
file.write("\nNew line added")
file.close()

#4. Read Line by Line
file = open("demo.txt", "r")
print(file.readline())
file.close()

#5. using with taht do not need manualy close file
with open("demo.txt", "r") as file:
    print(file.read())
 
 #create a file i want to delete it
file = open("new.txt", "w")
file.write("New file created")
file.close()

#delete file 
os.remove("new.txt")