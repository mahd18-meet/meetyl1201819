

def newlist(x):
	a=[x[0],x[-1]]
	return a
b=[1,2,3]
y=newlist(b)
print(y)


list1= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

list2=[]
for number in list1:
	if number < 5:
		print(number)
		list2.append(number)
print(list2)


user_option=int(input("enter a number"))
user_option_list=[]
for number1 in list1:
	if number1<int(user_option):
		user_option_list.append(number1)
print(user_option_list)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
com_num=[]

for number in b:
	if number in a:
		com_num.append(number)
print(com_num)


num=int(input("enter a number"))
if num>1:
	for i in rangle(2,num):
		if (num%i)==0:
			print(num+" is a prime number")
		else:
			print(num+ " is not a prime number")
else:
	print(num+" is not a prime number")
