#import math, decimal
#My First Python Code

print("Hello world")

name = input("What's you name? ")

print("Nice to meet you,", name)

age = input("What's your age? ")

age = int(age) #can check type of object by using type("name")

if(age == 20):
    print("We're the same age!")
elif (age >20):
    print("You're older than me.")
else:
    print("You're younger than me.")
print("So", name + ", what's your favorite food?")
food = input()
if(food == "pizza" or food=="Pizza"):
	print("Mine, too!")
else:
	print("Oh cool, that's a good choice!")
print("Well", name +"," , "it was nice meeting you!", "I hope you get some", food, "soon")

#Demonstrating Integers

# x,y,z = 1,2,3

# print(x, y, z)

# def intEx(): #function (has to be defined above like c++)
#     x = 5
#     y = 2
#     cats = "cats"
#     print(x, "^", y, " = ", x ** y)
#     print("I have {} {}".format(y,cats))

#     for i in cats: #for-each loop
#         print(i)

# intEx() #calling function

# for i in range(0,10,2): #for loop incremented by two
#     print(i)
