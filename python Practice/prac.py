file = open("socialSec.txt","a+")
while(True):
    name = input("Enter a name and social\n")
    file.write("Name and Social: " + name + "\n")
    file.flush()