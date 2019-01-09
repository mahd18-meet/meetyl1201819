from turtle import *
import turtle

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.penup()
		self.shape("circle")
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shapesize(r/10)
		self.color(color)
		self.goto(x, y)
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.screen_width=screen_width
		self.screen_height=screen_height
		self.goto(new_x,new_y)
		if (new_x>screen_width) or (new_x<-screen_width):
			self.dx = -self.dx
		if (new_y>screen_height) or (new_y<-screen_height):
			self.dy=-self.dy
		
# s=Ball(0,0,3,5,50,"red")

# while True:
# 	s.move(420,350)

