import turtle

print ("Noor")
print ("Noor"*3)
print ("Noor"*100)
number1=4
number2=number1/2
numbers=[1,2,3]
sums=0
for number in numbers:
	print(number*2)
	sums=sums+1
print(sums)


turtle.begin_fill()
turtle.pendown()
turtle.goto(0,50)
turtle.goto(50,50)
turtle.goto(50,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.penup()

turtle.goto(100,100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.pencolor(blue)
turtle.goto(-100,50)
turtle.pendown()
turtle.circle(100)





turtle.mainloop()