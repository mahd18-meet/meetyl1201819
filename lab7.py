from turtle import *
import random
import math
import turtle
turtle.colormode(255)

width=300
height=300

class Ball(Turtle):
	def __init__(self,radius,color,dx,dy):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color)
		self.dx=dx
		self.dy=dy
	def move(self):
		oldx=self.xcor()
		oldy=self.ycor()
		newx=oldx+self.dx
		newy=oldy+self.dy
		self.goto(newx,newy)
		if (newx>width) or (newx<-width):
			self.dx = -self.dx
		if newy>height or newy<-height:
			self.dy=-self.dy
		




ball1=Ball(50,"green",2,3)
ball2=Ball(40,"blue",5,7)

def check_collision(balla,ballb):
	x1=balla.xcor()
	x2=ballb.xcor()
	y1=balla.ycor()
	y2=ballb.ycor()
	r1=balla.radius
	r2=ballb.radius
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if r1+r2<D:
		print("The balls did not collide")
	elif r1+r2>D or r1+r2==D:
		rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		balla.color(rgb)
		ballb.color(rgb)
		if balla.radius>ballb.radius:
			smaller=ballb
		else:
			smaller=balla
		smaller.goto(random.randint(-300,300),random.randint(-300,300))

while True:
	ball1.penup()
	ball2.penup()
	ball1.move()
	ball2.move()
	ballslist=[ball1,ball2]
	check_collision(ball1,ball2)



turtle.mainloop()