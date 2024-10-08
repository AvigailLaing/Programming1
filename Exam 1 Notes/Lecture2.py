#Module 2 (Lecture 3)

var = 23
var_2 = 56
var3 = var + var_2
print(var3)

# a, b = 56, 78
# c = a + b
# print(c)

#Never use key words when naming your variables!

# a = input("Enter number 1: ")
# b = input("Enter number 2: ")
# c = a + b
# #This code does not add the two numbers, it just lists the two strings one after the other because the input function automatically takes strings
# print(c)

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = a + b
# print(c)
#
# #We have to change the input to floating if we want to use decimals, and we can also use a round function
# d = float(input("Enter number 1: "))
# e = float(input("Enter number 2: "))
# f = d + e
# print(f)
# print(round(f))


# a = 2.5
# b = 3.5
# print(round(a))
# print(round(b))
#This prints 2 and 4 because there is a rule that rounds to the nearest even number
#For things like 2.5 it rounds to 2, but for 3.5 it rounds to 4 since it goes to the next even number

# x = 3.5675
# print(round(x, 2))
#This rounds x to two decimal places

name = "John"
age = 45
print("The name is", name, "his age is", age)
#\n gives you a new line \t gives you a tab
#By default, we have a space after is that comes between John, this is because of sep,
#which by default is set to a space
print("The name is", name, "his age is", age, sep = "***")

print("The name is", name, sep="!", end="....")
print("his age is", age)
#By default, when we run a command it prints on a new line because of the end parameter
#The end parameter by default is \n

# a = "Hello"
# b = "World"
# print(a + b)
# #If it is a string, the print function can be used to concatenate

a = 5.4444
b = 10.33
c = a + b
print(f"The sum of {a} and {b} is {c}")
print(f"The sum of a and b is {c:.2f}")
#How we reduce to 2 decimal places

x = 10
y = 3
r = x % y + 2 * x//y
print(r)
#Final answer is 7

d = 500
d = 500 + 1
print(id(d))
print(id(500))
e = 500
#This is an object, all objects have a type, value, and identity
print(type(d))
print(id(d))
print(id(e))
#ID D and E are the same because they are referencing the same object of 500
