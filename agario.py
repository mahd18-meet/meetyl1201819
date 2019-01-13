import time
import turtle
import random
from ball import Ball 
import math

turtle.tracer(1)
turtle.hideturtle()
RUNNING = True 
SLEEP = 0.0077
screen_width = turtle.getcanvas().winfo_width()/2
screen_height =  turtle.getcanvas().winfo_height()/2


number_of_balls=2
minimum_ball_radius=10
maximum_ball_radius=100
minimum_ball_dx=-5
maximum_ball_dx=5
minimum_ball_dy=-5
maximum_ball_dy=5
balls=[]

for i in range(number_of_balls):
	x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
	y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
	print(x, y)
	dx=random.randint( minimum_ball_dx, maximum_ball_dx)
	dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	radius=random.randint(minimum_ball_radius,maximum_ball_radius)
	color=(random.random(), random.random(), random.random())
	while dx == 0:
		dx=random.randint( minimum_ball_dx, maximum_ball_dx)
	while dy==0:
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	new_ball=Ball(x,y,dx,dy,radius,color)
	balls.append(new_ball)


def collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False
	x1=ball_a.xcor()
	x2=ball_b.xcor()
	y1=ball_a.ycor()
	y2=ball_b.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D >= ball_a.r + ball_b.r:
		print("no collision")
		return False
	if D < ball_a.r + ball_b.r:
		print("COLLISION")
		return True

def check_all_balls():
	for ball_a in balls:
		for ball_b in balls:
			collide(ball_a,ball_b)
			

def move_all_balls():
	while True:
		for o in balls:
			o.move(screen_width, screen_height)
			check_all_balls()

if check_all_balls() == True:
	r1=ball_a.r
	r2=ball_b.r

	x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
	y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
	print(x, y)
	dx=random.randint( minimum_ball_dx, maximum_ball_dx)
	dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	radius=random.randint(minimum_ball_radius,maximum_ball_radius)
	color=(random.random(), random.random(), random.random())
	while dx == 0:
		dx=random.randint( minimum_ball_dx, maximum_ball_dx)
	while dy==0:
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)

	



move_all_balls()
check_all_balls(ball_a,ball_b)
turtle.update()
turtle.mainloop()