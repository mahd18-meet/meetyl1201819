import time
import turtle
import random
from ball import Ball 

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =  turtle.getcanvas().winfo_height()/2


number_of_balls=5
minimum_ball_radius=10
maximum_ball_radius=100
minimum_ball_dx=-5
maximum_ball_dx=5
minimum_ball_dy=-5
maximum_ball_dy=5
balls=[]

for i in range(number_of_balls):
	x=random.randint(-SCREEN_WIDTH+ maximum_ball_radius,SCREEN_WIDTH - maximum_ball_radius)
	y=random.randint( -SCREEN_HEIGHT + maximum_ball_radius,SCREEN_HEIGHT - maximum_ball_radius)
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




turtle.update()
turtle.mainloop()