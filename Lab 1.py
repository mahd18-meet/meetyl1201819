import turtle
'''
print ("Noor")
print ("Noor"*3)
print ("Noor"*100)
number1=4
number2=number1/2
numbers=[1,2,3]
sums=0
for number in numbers:
	print(number*2)
	sums=sums+number
print(sums)
'''
'''
turtle.begin_fill()
turtle.pendown()
turtle.goto(0,50)
turtle.goto(50,50)
turtle.goto(50,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.penup()
'''
'''
def circle():
	turtle.penup()
	turtle.goto(100,100)
	turtle.pendown()
	turtle.pensize(15)
	turtle.circle(100)
	return circle()
'''
turtle.pensize(10)

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(50)
turtle.penup()

turtle.goto(-150,-50)
turtle.pendown()
turtle.pencolor("yellow")
turtle.circle(50)
turtle.penup()

turtle.goto(-100,0)
turtle.pendown()
turtle.pencolor("black")
turtle.circle(50)
turtle.penup()

turtle.goto(-50,-50)
turtle.pendown()
turtle.pencolor("green")
turtle.circle(50)
turtle.penup()

turtle.goto(0,0)
turtle.pendown()
turtle.pencolor("red")
turtle.circle(50)

turtle.mainloop()