
import tkinter as tk
from tkinter import *


greeting = simpledialog.askstring("Input","Hello, possible pirate!")
if greeting in ["Arrr!"]:
	print ("Go away, pirate.")
else:
	print ("Greetings, hater of pirates!")
	'''

#a time traveler has suddenly appeared in your classroom!
#create a variable representing the traveler's year of origin (e.g., year = 2000)
#and greet our strange visitor with a different mesage
#if he is from the distant past (before 1900),
#the present era (1900-2020) or from the far future (beyond 2020)
import tkinter as tk
from tkinter import simpledialog
year == int.simpledialog.askstring("Input","Greetings! what is your year of origin?, parent=tk.Tk().withdraw()")
if year<-1900:
	print("woah, what's the past!")
elif year>1900 and year <2020:
	print("that's totally the present!")
else:
	print("far out, that's the future!!")
'''


'''
class cat():
	def __init__(self, name, age):
		self.name=name
		self.age = 0
	def birthday(self,age):
		self.age +=1
		if self.age>=100:
			print("Dong dong, the cat is dead!")
		else:
			print(self.name, 'hasing its', self.age, 'birthday!')
my_cat= cat ("Salem",8)
my_cat.birthday(8)
#what i want: my cat to celebrate its 8th birthday (and all the birthdays
#that come before that)
'''
'''
class Cake():
	def __init__(self,flavor):
		self.flavor=flavor
	def eat(self):
		print("Yummy!!! Eating a",self.flavor," cake! :)")
cake=Cake("chocolate")
print(cake.eat())
'''