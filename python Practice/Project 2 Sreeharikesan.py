'''
Project 2 - Scores Analysis and Bar Chart - Spring 2020
Author: <Saran Sreeharikesan 906044343>

This program <describe your program here>.

I have neither given or received unauthorized assistance on this assignment.
Signed:  <Saran>
'''
import turtle
import random

def draw_bar():
    A=0
    B=0
    C=0
    D=0
    F=0
    turtle.setup(1000, 1000)
    turtle.title('Project 2 - Bar Chart')
    turtle.speed(0)
    
    def rgb():
        r = random.random()
        g = random.random()
        b = random.random()
        return (r, g, b)
    
    def bar(grade,x,y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.fillcolor(rgb())
        turtle.pensize(4)
        turtle.pencolor('black')
        turtle.pendown()
        turtle.begin_fill()
        turtle.setheading(90)
        turtle.forward(grade*2000)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(grade*2000)
        turtle.right(90)
        turtle.forward(200)
        turtle.end_fill()
        
    def label(x, word):
        turtle.penup()
        turtle.goto(x,-425)
        turtle.pendown()
        turtle.write(word,align='center')
        
    for i in range(len(avg)):
        if avg[i]>=90:
            A+=1
        elif avg[i]>=80:
            B+=1
        elif avg[i]>=70:
            C+=1
        elif avg[i]>=60:
            D+=1
        else:
            F+=1

    A/=len(avg)
    B/=len(avg)
    C/=len(avg)
    D/=len(avg)
    F/=len(avg)

    bar(A,-500,-500,rgb())
    bar(B,-300,-500,rgb())
    bar(C,-100,-500,rgb())
    bar(D,100,-500,rgb())
    bar(F,300,-500,rgb())
    
    label(-400,'90s')
    label(-200,'80s')
    label(0,'70s')
    label(200,'60s')
    label(400,'<60s')
    
    turtle.hideturtle()
    
proceed='y'
while proceed=='y' or proceed=='Y':
    line=0
    file=open(input('Please enter the file name: '))
    line=file.readlines()
    print('Results for', line[0])
    print('Number of scores: ',len(line[1:]))
    print('High score: ',max(line[1:]),end='')
    print('Low score: ',min(line[1:]),end='')
    avg = list(map(int, line[1:]))
    average=(sum(avg)/len(avg))
    print('Average: ',round(average,2))
    draw_bar()
    proceed=input('Process another file (y or n)? ')
    turtle.reset()
print()
print('Have a good day!')


