import time
import turtle
import random
from ball import Ball 
import math

turtle.tracer(0)
turtle.hideturtle()
wn=turtle.Screen()
RUNNING = True 
SLEEP = 0.0077
screen_width = turtle.getcanvas().winfo_width()/2
screen_height =  turtle.getcanvas().winfo_height()/2

turtle.register_shape("food.gif")

MY_BALL=Ball(0,0,3,5,30,"red")
number_of_balls=5
number_of_food=10
minimum_ball_radius=10
maximum_ball_radius=90
minimum_ball_dx=-5
maximum_ball_dx=1
minimum_ball_dy=-5
maximum_ball_dy=1
balls=[]
FOODS=[]

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
	food.shape("food.gif")
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

def eat_food():
	x=random.randint(-screen_width+ maximum_ball_radius,screen_width - maximum_ball_radius)
	y=random.randint( -screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)

	for food in FOODS:
		if collide(MY_BALL, food) == True:
			MY_BALL.r=MY_BALL.r+0.5
			MY_BALL.shapesize(MY_BALL.r/10)
			food.goto(x,y)



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
turtle.update()

while RUNNING:
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height =  turtle.getcanvas().winfo_height()/2
	check_all_balls()
	move_all_balls()
	eat_food()
	RUNNING=check_myball_collision(MY_BALL)
	turtle.update()
	time.sleep(SLEEP)
	
if RUNNING ==False:
	print("Game over!")
turtle.mainloop()