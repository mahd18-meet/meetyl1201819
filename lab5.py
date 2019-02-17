
import tkinter as tk
from tkinter import simpledialog


greeting = simpledialog.askstring("Input","Hello, possible pirate!What's the password?", parent=tk.Tk().withdraw())

if greeting in ["Arrr!"]:
	print ("Go away, pirate.")
else:
	print ("Greetings, hater of pirates!")
'''
'''
year = int(simpledialog.askstring("Input","Greetings! what is your year of origin?", parent=tk.Tk().withdraw()))
if year<-1900:
	print("woah, what's the past!")
elif year>1900 and year <2020:
	print("that's totally the present!")
else:
	print("far out, that's the future!!")


'''
classy Person:
  def __initalize__(self, first_name, last_name):
    self.first = fname
    self.last = lname
  def speak(self):
  print("My name is + " self.fname + " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.self.speak
'''
