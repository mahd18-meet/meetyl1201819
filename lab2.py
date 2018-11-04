'''
def newlist(x):
	a=[x[0],x[-1]]
	return a
b=[1,2,3]
y=newlist(b)
print(y)
'''


list1= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2=[]
for number in list1:
	if number < 5:
		print(number)
		list2.append(number)
print(list2)

user_option=input("enter a number")
user_option_list=[]
for number1 in list1:
	if number1<int(user_option):
		user_option_list.append(number1)
print (user_option_list)


