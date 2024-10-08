#Built-in types are numeric or sequence (ordered collection of objects)
#Or containers, which are unordered
str = "Python"
print(str)
#Indexing starts with 0
print(str[0]) #will print P

#range(start, limit, step)
print(str[1:5])
#this prints ytho
print(str[1:5:2])
#this will start with y, go up 2, print h, then not print str[5] because
#the range is exclusive of the last value
print(str[0], str[2:4])
#this will print P th

print(str[-1])
#this gives you the last element n
#index backwards starts with -1, -2, -3, -4, -5
print(str[-1:-4])
#this by itself with not work because default step value is 1
print(str[-1:-4:-1])
#this will work because step value is -1, so it can go back to -3

print(str[:5])
#this by default takes the start value as 0
#so this will go 0-5

#str = "python"
#str[1] = "z"
#note how this will NOT work because strings are immutable
#print(str)

course_num = 3502

#this must be changed to a string on len won't work :)
welcome = "Hello"
name = "Avigail"
print(welcome + name)
#this prints HelloAvigail

#ASCII code
print(ord("a")) #will print the ASCII code for lowercase a
print(chr(98)) #will print the character for the ASCII code

hex_digit = "C" #12
print(ord("A")) #10
print(ord(hex_digit) - ord("A") + 10)
#so this finds how far away C is from A, which we know is 10 in hexadecimal
#and it then adds that distance to 10 to create the hexadecimal equivalent

original_list = [1,2,3,4,5,6,7,8,9]
sliced_list = original_list[0::4]
#NEW ONE
#Put in Module 7 notes and notebook
#0:end:4
#1, 5, 9
#Sum will be 15
print(sum(sliced_list))
sliced_list = original_list[0:8:4]
#This, however, will not give you the last element
#But when you do [0::4], it WILL give you the last element