
class Animal(object):
	def __init__(self, sound, name, age, favorite_color):
		self.sound= sound
		self.name= name
		self.age= age
		self.favorite_color= favorite_color
	def eat(self, food):
		print("Yummy! " + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is " + self.age +" years old and loves the color " + self.favorite_color)
	def make_sound(self,number):
		self.number = number
		print(self.sound*number)

cat = Animal("meow","kitty","3","red")
cat.eat("meat")
cat.description()
cat.make_sound(2)


class Person(object):
	def __init__(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def fav_breakfast(self, food):
		print(self.name + "'s favorite breakfast is "+food)
	def fav_sport(self,sport):
		print("His favorite sport is "+sport)

Matt=Person("Matt", "20", "Jerusalem", "Male")
Matt.fav_breakfast("cereal")
Matt.fav_sport("football")



class Song(object):
	def __init__(self,lyrics):
		self.lyrics= lyrics
	def singmeasong(self):
		print(self.lyrics)

despacito=Song("DEEESPAAAACITO despacito")
despacito.singmeasong()
flower_song=Song(["roses are red",
				"violets are blue",
				"I wrote this poem for you."])
for line in flower_song.lyrics:
	print (line)
