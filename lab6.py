
import random
import turtle
from turtle import *
colormode(255)
global height
height = None

class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		self.width = width
		self.height  = height
		turtle.register_shape("rectangle", ((50,0),(50,30),(0,30),(0,0)))
		self.shape("rectangle")
		self.setheading(90)

	def random_color(self):
		rgb = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
		self.fillcolor(rgb)

Jimmy = Rectangle(10,20)
Jimmy.random_color()


class Square(Rectangle):
	def __init__(self,size):
		Rectangle.__init__(self,size,size)
		self.shapesize(size)
		self.pencolor("BLUE")
		self.pensize(5)
		self.shape("square")

	def random_color(self):
		rgb = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
		self.fillcolor(rgb)

Judeh= Square(4)
Judeh.random_color()


class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.pencolor("RED")
		self.begin_poly()
		for i in range(5):
			self.left(72)
			self.fd(50)			
		self.end_poly()
		p = self.get_poly()
		register_shape("hexagon", p)
		self.fd(100)
		self.shape("hexagon")
		self.setheading(90)

Juj = Hexagon(1)


class Polygon(Turtle):
	def __init__(self,num_of_sides,side_length,angle):
		Turtle.__init__(self)
		self.shapesize(1)
		self.pencolor("yellow")
		self.pensize(5)
		for i in range(num_of_sides):
			self.fd(side_length)
			self.left(angle)

#user enters and edits the angle and length of the sides

k=Polygon(6,100,60)

hexagon=Polygon(5,50,72)


turtle.mainloop()