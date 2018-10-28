import turtle
'''
#q1
angle=150
length=200
turtle.pensize(10)
for i in range(5):
	turtle.forward(length)
	turtle.right(angle)
'''
'''
#q2

import turtle
turtle.begin_fill()
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(30)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(30)
turtle.forward(50)
turtle.end_fill()

turtle.mainloop()

'''
forward=200
forward2=100

for r in range(100):
	turtle.forward(forward)
	turtle.right(30)
	turtle.forward(forward2)
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.right()

turtle.mainloop()