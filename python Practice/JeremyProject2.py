import turtle

def draw_plot():
    turtle.reset()
    turtle.setup(width=500, height=300, startx=200, starty=200)
    turtle.colormode(255)
    turtle.speed('fastest')
    turtle.pensize(2)
    turtle.title(lines[0])
    ninety = 0
    eighty = 0
    seventy = 0
    sixty = 0
    other = 0
    for score in scores:
        if score >= 90:
            ninety+=1
        elif score >= 80:
            eighty+=1
        elif score >= 70:
            seventy+=1
        elif score >= 60:
            sixty+=1
        else:
            other+=1
    scalar = 500
    ninety = ninety/len(scores) * scalar
    eighty = eighty/len(scores) * scalar
    seventy = seventy/len(scores) * scalar
    sixty = sixty/len(scores) * scalar
    other = other/len(scores) * scalar

    def draw_bar(x,y,text,length,r,g,b,width):
        turtle.penup()
        turtle.goto(x,y)
        turtle.fillcolor(r,g,b)
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(length)
        turtle.setheading(0)
        turtle.forward(width)
        turtle.setheading(270)
        turtle.forward(length)
        turtle.setheading(180)
        turtle.forward(width)
        turtle.penup()
        turtle.end_fill()
        turtle.goto(x+30,-90)
        turtle.pendown()
        font = ("Arial", 10, "bold")
        turtle.write(text, align='center',font=font)

    x,y = -150,-100
    width = 60
    draw_bar(x,y,'90%',ninety,0,255,0,width)
    x+=width
    draw_bar(x, y, '80%', eighty, 102, 255, 102,width)
    x += width
    draw_bar(x, y, '70%', seventy, 255, 255, 102, width)
    x += width
    draw_bar(x, y, '60%', sixty, 255, 178, 102, width)
    x += width
    draw_bar(x, y, '<60%', other, 255, 0, 0, width)

    turtle.hideturtle()


user_input = 'y'
while user_input.lower() == 'y':
    file_name = input('Please enter the file name: ')
    lines = open(file_name,'r').readlines()
    scores = list(map(int, lines[1:]))
    print('Results for',lines[0], end='')
    print('Number of scores:', len(scores))
    print('High score:', max(scores))
    print('Low score:', min(scores))
    print('Average score:', round(sum(scores) / (len(lines)-1),2), end='\n\n')
    draw_plot()
    user_input = input('Process another file (y or n)? ')
    print()
print('Goodbye!')
