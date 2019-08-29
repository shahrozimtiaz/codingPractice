# file = open("engToSpanish.txt", "r")
# lines = file.readlines()
dictionary = {}
# for line in lines:
#     line.replace("\t", " ")
#     key = line[:line.find(" ")].strip()
#     print(key)
#     value = line[line.find("\t"):].strip()
#     dictionary[key]=value

dictionary["mother"]="madre"
dictionary["run"]="correr"
while(True):
    key = input("Enter the word to be translated \n")
    value = dictionary.get(key)
    print(key, "->", value)