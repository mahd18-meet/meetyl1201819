
import random
import turtle
from turtle import *
colormode(255)
'''
class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)

	def random_color(self):
		rgb = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
		self.fillcolor(rgb)

Judeh = Square(10)
Judeh.random_color()
'''
'''
class Rectangle(Turtle):
	def __init__(self,width, height):
		Turtle.__init__(self)
		self.width = width
		self.height  = height
		turtle.register_shape("rectangle",((50,0),(50,30),(0,30),(0,0)))
		self.shape("rectangle")

	def random_color(self):
		rgb = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
		self.fillcolor(rgb)

Jimmy = Rectangle(10,20)
Jimmy.random_color()
'''









turtle.mainloop()