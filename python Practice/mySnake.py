# Shahroz Imtiaz
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

curses.initscr()
win = curses.newwin(20,60, 0, 0)
curses.noecho()
curses.cbreak
win.keypad(True)
curses.curs_set(False)
win.nodelay(True)
win.border(0)

win.addstr(0,21,"KEVIN DURANT Snake Game")

food  = [randint(1,18),randint(1,58)]
snake = [ [8,30], [8,29], [8,28] ]

key = KEY_RIGHT
prevKey = key

score = 0;

while(key!=27):
	win.timeout(100)
	win.addstr(0,0,"Score: " + str(score))

	win.addch(food[0],food[1], '*')
	for i in range(len(snake)):
		win.addch(snake[i][0],snake[i][1], 'o')

	key = win.getch()
	if(key==-1):
		key=prevKey
	prevKey=key

	if(key==KEY_LEFT):
		snake.insert(0, [snake[0][0],snake[0][1]-1])
		erase = snake.pop()
		win.addch(erase[0],erase[1], ' ')
	if(key==KEY_RIGHT):
		snake.insert(0, [snake[0][0],snake[0][1]+1])
		erase = snake.pop()
		win.addch(erase[0],erase[1], ' ')
	if(key==KEY_UP):
		snake.insert(0, [snake[0][0]-1,snake[0][1]])
		erase = snake.pop()
		win.addch(erase[0],erase[1], ' ')
	if(key==KEY_DOWN):
		snake.insert(0, [snake[0][0]+1,snake[0][1]])
		erase = snake.pop()
		win.addch(erase[0],erase[1], ' ')

	if(snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 60 or snake[0] in snake[1:]):
		break

	if(snake[0]==food):
		score+=1;
		snake.insert(0, [food[0],food[1]])
		food  = [randint(1,18),randint(1,58)]
curses.endwin()
print("Score: " + str(score))
print("Thanks for playing :)")