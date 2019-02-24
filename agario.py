import time
import turtle
import random
from ball import Ball 
import math
import tkinter as tk
from tkinter import *


turtle.register_shape("black cat.gif")
turtle.register_shape("dog.gif")
turtle.register_shape("tom.gif")
turtle.register_shape("son.gif")
turtle.register_shape("meathead.gif")
turtle.register_shape("jerry1.gif")
turtle.register_shape("jerry2.gif")
turtle.register_shape("jerry3.gif")
turtle.register_shape("jerry4.gif")
turtle.register_shape("nibbles.gif")

turtle.register_shape("brain.gif")
turtle.register_shape("chemistry.gif")
turtle.register_shape("dna.gif")
turtle.register_shape("english.gif")
turtle.register_shape("globe.gif")
turtle.register_shape("idea.gif")
turtle.register_shape("math.gif")
turtle.register_shape("xoxo.gif")

turtle.register_shape("brain.gif")
turtle.register_shape("brain(1).gif")
turtle.register_shape("brain(2).gif")
turtle.register_shape("brain(3).gif")

turtle.tracer(0)
turtle.hideturtle()
wn=turtle.Screen()
gameover=turtle.clone()
gameover.penup()
gameover.hideturtle()
gameover.goto(50,100)
RUNNING = True
SLEEP = 0.0077
screen_width = turtle.getcanvas().winfo_width()//2
screen_height =  turtle.getcanvas().winfo_height()//2
MY_BALL=Ball(0,0,3,5,30,"red")
MY_BALL.shape("brain.gif")

number_of_balls=4
number_of_food=5
minimum_ball_radius=10
maximum_ball_radius=90
minimum_ball_dx=-1
maximum_ball_dx=1
minimum_ball_dy=-1
maximum_ball_dy=1
balls=[]
FOODS=[]
brains=["brain.gif","brain(1).gif","brain(2).gif","brain(3).gif","brain.(4).gif"]
subjects=["chemistry.gif","english.gif","globe.gif","idea.gif","math.gif","dna.gif","xoxo.gif"]
mice=["jerry1.gif","jerry2.gif","jerry3.gif","jerry4.gif"]
predators=["black cat.gif","son.gif","meathead.gif","dog.gif"]

def start_educational_game():
	for i in range(number_of_balls):
		x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
		y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
		
		dx=random.randint( minimum_ball_dx, maximum_ball_dx)
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)
		r=random.randint(minimum_ball_radius,maximum_ball_radius)
		color=(random.random(), random.random(), random.random())
		while dx == 0:
			dx=random.randint( minimum_ball_dx, maximum_ball_dx)
		while dy==0:
		 	dy=random.randint(minimum_ball_dy,maximum_ball_dy)
		new_ball=Ball(x,y,dx,dy,r,color)
		if (new_ball.r == 30) or (new_ball.r > 30 and new_ball.r < 50) or (new_ball.r < 30):
			new_ball.shape("brain.gif")
		if (new_ball.r == 50) or (new_ball.r > 50 and new_ball.r < 70):
			new_ball.shape("brain(1).gif")
		if (new_ball.r == 70) or (new_ball.r > 70 and new_ball.r < 90):
			new_ball.shape("brain(2).gif")
		if (new_ball.r == 90):
			new_ball.shape("brain(3).gif")
		balls.append(new_ball)
		
	for i in range(number_of_food):
		x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
		y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
		
		dx=random.randint( minimum_ball_dx, maximum_ball_dx)
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)
		r=5
		while dx == 0:
			dx=random.randint( minimum_ball_dx, maximum_ball_dx)
		while dy==0:
			dy=random.randint(minimum_ball_dy,maximum_ball_dy)
		food=Ball(x,y,dx,dy,r,color)
		i=random.randint(0,len(subjects)-1)
		food.shape(subjects[i])
		FOODS.append(food)

def start_casual_game():
	for i in range(number_of_balls):
		x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
		y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
		
		dx=random.randint( minimum_ball_dx, maximum_ball_dx)
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)
		r=random.randint(minimum_ball_radius,maximum_ball_radius)
		color=(random.random(), random.random(), random.random())
		while dx == 0:
			dx=random.randint( minimum_ball_dx, maximum_ball_dx)
		while dy==0:
		 	dy=random.randint(minimum_ball_dy,maximum_ball_dy)
		new_ball=Ball(x,y,dx,dy,r,color)
		i=random.randint(0,len(predators)-1)
		new_ball.shape(predators[i])
		balls.append(new_ball)
		
	for i in range(number_of_food):
		x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
		y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
		
		dx=random.randint( minimum_ball_dx, maximum_ball_dx)
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)
		r=5
		while dx == 0:
			dx=random.randint( minimum_ball_dx, maximum_ball_dx)
		while dy==0:
			dy=random.randint(minimum_ball_dy,maximum_ball_dy)
		food=Ball(x,y,dx,dy,r,color)
		i=random.randint(0,len(mice)-1)
		food.shape(mice[i])
		FOODS.append(food)

def collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False
	x1=ball_a.xcor()
	x2=ball_b.xcor()
	y1=ball_a.ycor()
	y2=ball_b.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D >= ball_a.r + ball_b.r:
		return False
	if D < ball_a.r + ball_b.r:
		return True

def eat_subjects():
	for food in FOODS:
		x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
		y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)

		if collide(MY_BALL, food) == True:
			MY_BALL.r=MY_BALL.r+0.5
			MY_BALL.shapesize(MY_BALL.r/10)
			food.goto(x,y)
			i=random.randint(0,len(subjects)-1)
			food.shape(subjects[i])
		for ball_a in balls:
			if collide(ball_a,food) == True:
				if ball_a.r <= 30:
					ball_a.r=ball_a.r+0.5
					ball_a.shapesize(ball_a.r/10)
					food.goto(x,y)
					i=random.randint(0,len(subjects)-1)
					food.shape(subjects[i])
				if ball_a.r > 30:
					food.goto(x,y)
					i=random.randint(0,len(subjects)-1)
					food.shape(subjects[i])

def eat_jerry():
	for food in FOODS:
		x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
		y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)

		if collide(MY_BALL, food) == True:
			MY_BALL.r=MY_BALL.r+0.5
			MY_BALL.shapesize(MY_BALL.r/10)
			food.goto(x,y)
			i=random.randint(0,len(mice)-1)
			food.shape(mice[i])
		for ball_a in balls:
			if collide(ball_a,food) == True:
				if ball_a.r <= 30:
					ball_a.r=ball_a.r+0.5
					ball_a.shapesize(ball_a.r/10)
					food.goto(x,y)
					i=random.randint(0,len(mice)-1)
					food.shape(mice[i])
				if ball_a.r > 30:
					food.goto(x,y)
					i=random.randint(0,len(mice)-1)
					food.shape(mice[i])

def randomize(ball1,ball2):
	x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
	y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
	dx=random.randint( minimum_ball_dx, maximum_ball_dx)
	dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	radius=random.randint(minimum_ball_radius,maximum_ball_radius)
	color=(random.random(), random.random(), random.random())
	while dx == 0:
		dx=random.randint( minimum_ball_dx, maximum_ball_dx)
	while dy==0:
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	if ball1.r < 100:
		if ball2.r <= 30:
			ball1.r=ball1.r+1
			ball1.shapesize(ball1.r/10)
		elif ball2.r >30:
			ball1.r=ball1.r+3
			ball1.shapesize(ball1.r/10)
	ball2.x=x
	ball2.y=y
	ball2.dx=dx
	ball2.dy=dy
	ball2.r=radius
	ball2.color(color)
	ball2.shapesize(ball2.r/10)
	ball2.goto(x,y)

def check_all_balls():
	for ball_a in balls:
		for ball_b in balls:
			if collide(ball_a,ball_b) == True:
				r1=ball_a.r
				r2=ball_b.r

				if r1 > r2:
					randomize(ball_a,ball_b)
				else:
					randomize(ball_b,ball_a)

def move_all_balls():
	for o in balls:
		print (o)
		o.move(screen_width, screen_height)
			
def check_myball_collision(MY_BALL):
	for ball_a in balls:
 		if collide(MY_BALL,ball_a) == True:
 			r_1=ball_a.r
 			r_2=MY_BALL.r
 			if r_1 > r_2:
 				return False
 			if r_2 > r_1:
 				randomize(MY_BALL,ball_a)			
	return True

def movearound(event):
	MY_BALL.goto(event.x - screen_width, screen_height - event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

def Educational_function():
	turtle.bgpic("desk.gif")
	MY_BALL.shape("brain.gif")
	start_educational_game()
	RUNNING = True
	SLEEP = 0.0077
	while RUNNING:
		screen_width = turtle.getcanvas().winfo_width()//2
		screen_height =  turtle.getcanvas().winfo_height()//2
		check_all_balls()
		move_all_balls()
		eat_subjects()
		RUNNING=check_myball_collision(MY_BALL)
		turtle.update()
		time.sleep(SLEEP)
		
	if RUNNING == False:
		turtle.bgpic("no.gif")
		gameover.write("GAME OVER! :(", True, font=("CHARLESWORTH",30,"bold"))

def Casual_function():
	turtle.bgpic("background.gif")
	MY_BALL.shape("tom.gif")
	start_casual_game()
	RUNNING = True
	SLEEP = 0.0077
	while RUNNING:
		screen_width = turtle.getcanvas().winfo_width()//2
		screen_height =  turtle.getcanvas().winfo_height()//2
		check_all_balls()
		move_all_balls()
		eat_jerry()
		RUNNING=check_myball_collision(MY_BALL)
		turtle.update()
		time.sleep(SLEEP)
		
	if RUNNING == False:
		turtle.bgpic("no.gif")
		gameover.write("GAME OVER! :(", True, font=("CHARLESWORTH",30,"bold"))

root=tk.Toplevel()
root.title('WELCOME TO AGAR.IO!')
image1=tk.PhotoImage(file="collage.gif")
w=image1.width()
h=image1.height()
root.geometry("%dx%d+0+0" % (w, h))
panel1=tk.Label(root,image=image1)
panel1.pack(side='top', fill='both', expand='yes')
Educational = tk.Button(panel1, text='Educational', height=3, width=10, command=Educational_function, activebackground="cyan", activeforeground="blue") #command=
Educational.pack(side='top')
Casual = tk.Button(panel1, text='Casual', height=3, width=10, command=Casual_function, activebackground="yellow", activeforeground="green") #command=
Casual.pack(side='bottom')
panel1.image=image1
root.mainloop()	
turtle.mainloop()