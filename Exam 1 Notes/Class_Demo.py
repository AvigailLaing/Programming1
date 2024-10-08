#This is our first program
'''
multiline comment
comment 2
'''
print("Hello World")
print('Hello World, I"m at UF')
print('''He'llo World, I"m at UF''')

age_user = 13
#Use control forward slash to comment code

a = 22
b = 5
c = a + b
print("The sum of a and b is", c)
print("The sum of", a ,"and", b ,"is", c)
e = a/b
d = a//b
print(e)
print(d)

f = 10
g = 3
h = f**g
print(h)
i = f % g
print(i)
#Mod returns the remainder

#For some reason this works
j = 20
k = 30
l = k/j
m = k//j
print(l + m)

#This isn't working for some reason
# inp = input()
# print(inp)
#
# name= input('What is your name?')
# print(name)
#
# #More advanced
# prompt = 'What is your name?'
# yourName = input(prompt)
# print("Hello," + yourName+".")
#Not sure if the above line works right

#Things work differently when gathering numbers
# number = input('Type in a number from 1-10:\n')
# #Should give you a new line
# print(int(number))
# print(int(number) + 5)

#Lecture 3 notes
name = "Ashish"
a = 52
b = 56
c = a + b
print("The sum is", c)

c, d = 45, 78
e = c + d
print("The sum is", e, sep = '***')
#Parameter set as a space. if we don't want a space we can define it with these 3 astrices

f = "Hello"
g = "World"
h = f + g
print("The sum is", h)

i = 5
j = 10
k = 100
l = 90
m = i * (j + k) / l
print(m)
#This computed with PEMDAS, order of precedence
print("Value of i is", i, sep = "!", end = "***")
print("And value of j is", j)
#By default there is another parameter we can change, lines by default go to next line
#End by default is a new line, but now both will be on the same line
#By default, sep is a space and end is a new line, but if we want to change them we can