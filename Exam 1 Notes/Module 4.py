# Learning loops

# for i in range(1, 10+1, 3):
#     print(i)
#     #By default, range starts by 0, but if you put a value before the last one, it will start there
#     #(1,10) will print 1-9
#     #(10) will print 0-9
#     #1, 10+1 will print 1-10
#     #You can add a third parameter to change how much it increases by
#     #1, 10+1, 3 will do 1, 4, 7, 10
#
# str = "Python"
#
# for char in str:
#     print(char)


# n = 1
#
# while n<= 10:
#     print(n)
#     n +=1

#Factorial
#How can we write a program to calculate the factorial of a number?
# num = int(input("Enter a number: "))
# #We make separate variable f because we don't want to change num
# f = 1
# for i in range(1, num+1):
#     f = f*i
#     #Cumulative multiplication
# print(f)
#
# x = 5
# for i in range (1,5,3):
#     #x starts with 5 and then for i = 1, we add 10
#     #15, i jumps to 4, then we get another addition of 10 = 25
#     #now it won't run again since the upper limit is 5
#     x += 10
# print(x)

#Patterns
# **********
l = int(input("Enter the length: "))
#To print 5 rows of astrices with 5 columns (length = 5)
for i in range(1, l+1):
    for j in range (1, l+1):
        print('*', end="")
    #j does its job to print 5 astrices once, then the statement
    #underneath prints a line before the i loop iterates again
    #and the i loop iterates 5 times, making 5 rows
    print()
    #The end="" is important because otherwise it will print 5
    #astrices each on a different line

# we want to print 1 astrix one line, then 2 next line, then 3 up to 5
# we could do 4 blank spaces after the 1 astrix
#we think of this as a matrix
#i is equal to the row position, j is the column position
#if i>j, print an astrix, otherwise print a space
# for i in range(1, l+1):
#     for j in range(1, l+1):
#         if i >= j:
#             print('*', end = "")
         #Too complex, can make it easier, see below!!!
#         else:
#             print(' ', end = "")
#     #After j runs for all 5 columns on row 1, we move to the nxt line with print()
#     print()
#ideal length is 5
# we want to print 1 astrix one line, then 2 next line, then 3 up to 5

for i in range(1, l+1):
    for j in range(1, i+1):
    #when i is 1, your j will only work once now
        print('*', end ="")
    print()
#for patterns, find commonality of where things are printed based on row and column

x = 5
for i in range (2,4):
    x = x*10
    for j in range (1,3):
        x += x
print(x)

#i starts with 2, and then x becomes 50
#then j starts with 1, and x is added to itself (50 + 50) = 100
#the INNER LOOP KEEPS RUNNING! so 100 is added to itself again to get 200
#now i becomes 3 and 200 becomes 2000, then j restarts at 1
#2000 is added to itself when j = 1, then j = 2 and 4000 is added to itself
#and THE RESULT IS 8000

x = 5
for i in range (2,4):
    x = x*10
    break
    x = x+1
for j in range (1,3):
    x = x*10
    continue
    x = x+1
print(x)

#i starts with 2, x becomes 50, then it exits the for loop
#now the j loop starts with j = 1 and 50 becomes 500
#instead of hitting x = x + 1 the continue means j becomes 2
#and then 500 becomes 5000
#then 5000 is printed

