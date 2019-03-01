from turtle import *
import turtle
import time 
import random
import math
from functions import *
from tkinter import *
from characters import *

turtle.tracer(100,1)
turtle.register_shape("abed.gif")
turtle.register_shape("gameover.gif")

abed = Player (20)
abed.shape("abed.gif")
abed.shapesize(1)
abed.penup()
turtle.bgpic("tapperbg.gif")

RUNNING = True
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
foods=[burger,pizza,sushi]
FOODCOLLISION= False
table=Food(200,280,40)
table2=Food(200,70,40)
table3=Food(200,-150,40)
table4=Food(200,-360,40)
tables = [table,table2,table3,table4]
number = 0

def up():
	global direction
	direction=UP 
	abed.goto(abed.xcor(), abed.ycor() + 20)

def down():
    global direction
    direction = DOWN
    abed.goto(abed.xcor(), abed.ycor() - 20)

def left():
    global direction
    direction = LEFT
    abed.goto(abed.xcor() - 20, abed.ycor())

def right():
    global direction
    direction = RIGHT
    abed.goto(abed.xcor() + 20, abed.ycor())

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

def collide(ball_a,ball_b):
	x1=ball_a.xcor()
	x2=ball_b.xcor()
	y1=ball_a.ycor()
	y2=ball_b.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D >= ball_a.r + ball_b.r:
		return False
	if D < ball_a.r + ball_b.r:
		return True

def check_food_collision():
	for f in foods:
		if collide(abed,f) == True:
			f.showturtle()
			f.goto(abed.xcor(),abed.ycor())
				
	return True

def slide_food():
	for f in foods:
		for t in tables:
			if collide(f,t) == True:
				f.goto(t.xcor(),t.ycor())
				f.bk(200)

def check_player_food_collision():
	players = getplayers()
	for f in foods:
		for player in players:
			if collide(f,player) == True:
				f.hideturtle()
				p = random.randint(0,3)
				a = random.randint(0,4)
				player.goto(starting_positions[p])
				player.shape(shapes[a])
				player.setheading(0)
				if f == burger:
					f.goto(450, 290)
				elif f == pizza:
					f.goto(570, 130)
				elif f == sushi:
					f.goto(650, -50)			
	return True

def disposing():
	for f in foods:
		if collide(f,trash) == True:
			f.hideturtle()
			if f == burger:
				f.goto(450, 290)
			elif f == pizza:
				f.goto(570, 130)
			elif f == sushi:
				f.goto(650, -50)

alert=turtle.Turtle()
alert.color("red")
alert.hideturtle()
alert.penup()
alert.goto(-500,400)

tyabed=turtle.Turtle()
tyabed.penup()
tyabed.hideturtle()
tyabed.color("red")
tyabed.goto(400,-400)

cross = turtle.Turtle()
cross.hideturtle()
cross.penup()
cross.goto(140,265)
cross.pensize(5)
cross.pencolor("red")

# cross.goto(330,360)
# cross.pendown()
# cross.goto(140,265)
# cross.penup()
# cross.goto(140,360)
# cross.pendown()
# cross.goto(330,265)

def attack():
	global RUNNING
	players = getplayers()
	for p in players:
		for t in tables:
			if collide(p,t) == True:
				p.setheading(p.towards(abed))
				p.forward(0.01)
				if collide(p,abed) == True:
					# for i in range(3):
					# 	alert.write("YOU HAVE BEEN ATTACKED BY A HUNGRY STUDENT", True, font=("CHARLESWORTH",20,"bold"))
					# 	alert.clear()
					# 	time.sleep(1)
					# 	alert.goto(-500,400)
					RUNNING = False


turtle.listen()
frame = 0

while RUNNING:	
	check_food_collision()
	frame+=1
	if frame/1500 == 1:
		frame = 0
		spawn_player()
	move_players()
	check_player_food_collision()
	slide_food()
	disposing()
	attack()
	turtle.update()

if RUNNING == False:
	abed.hideturtle()
	# for player in players:
	# 	player.hideturtle()

	turtle.bgpic("gameover.gif")
	cross.goto(330,360)
	cross.pendown()
	cross.goto(140,265)
	cross.penup()
	cross.goto(140,360)
	cross.pendown()
	cross.goto(330,265)
	cross.penup()


	cross.goto(360,310)
	cross.color("black")
	cross.write("Abed", True, font = ("CHARLESWORTH",30,"bold"))
	tyabed.write("P.S: thank you Abed <3", True, font = ("CHARLESWORTH",20,"bold"))

turtle.mainloop()