from turtle import *
import random
import math
import turtle

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color)
		self.speed(speed)

ball1=Ball(50,"green",2)
ball2=Ball(40,"blue",5)
ball3=Ball(20,"yellow",4)
ball4=Ball(10,"red",7)
balls_list=[ball1,ball2,ball3,ball4]

ball1.penup()
ball2.penup()
ball1.goto(0,0)
ball2.goto(0,90)

def check_collision(ball1,ball2):
	x1=ball1.xcor()
	x2=ball2.xcor()
	y1=ball1.ycor()
	y2=ball2.ycor()
	r1=ball1.radius
	r2=ball2.radius
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if r1+r2<D:
		print("The balls did not collide")
	elif r1+r2>D or r1+r2==D:
		ball1.color("red")
		ball2.color("red")

f=check_collision(ball1,ball2)

	





turtle.mainloop()