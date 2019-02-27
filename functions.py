from turtle import *
import turtle

class Food(Turtle):
	def __init__(self, x, y, r):
		Turtle.__init__(self)
		self.penup()
		self.r = r
		self.hideturtle()
		self.goto(x,y)

turtle.hideturtle()

turtle.register_shape("burger1.gif")
turtle.register_shape("pizzaf.gif")
turtle.register_shape("sushi.gif")
burger = Food (450, 290, 75)
burger.shape("circle")
burger.shape("burger1.gif")
turtle.penup()
pizza = Food (570, 130, 75)
pizza.shape("pizzaf.gif")
sushi = Food (650, -50, 75)
sushi.shape("sushi.gif")
turtle.tracer(1)

class Player(Turtle):
	def __init__(self,r):
		Turtle.__init__(self)
		self.penup()
		self.goto(150,0)

		self.r=r


class Table(Turtle):
	def __init__(self, x,y,r):
		Turtle.__init__(self)
		self.goto(x,y)
