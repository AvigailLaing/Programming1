my_list = [23, 56, 78, 89]
print(my_list[1:3])
#this WORKS LIKE A RANGE, so it only prints index 1 and 2, NOT THREE
#it is exclusionary of the last value in the range
#this prints [56, 78]
print(my_list[-3])
#negative indexing starts at -1
#this somehow works even though we didn't set the range step to -1????
#range step only needed if you do like [-3:-4]

my_list = ["first", "second", "third", "fourth"]
print(my_list[0], my_list[2])
#this will print first third
print(my_list[0:3])
#this will be a range one, so it will print from 0 to 2
#it will print ['first', 'second', 'third'] (DIF FORMAT)
#IMPORTANT EXAMPLE
print(my_list[:-1])
#this will go from 0 to -1 I believe
#this prints ['first', 'second', 'third']
#so it starts at 0 and goes 1 and 2 and then doesn't print 3 because 3 is equivalent to -1
#IMPORTANT EXAMPLE
print(my_list[-3:])
#COLON AFTERWARD
#-3 is equivalent to "second"
#this is saying we get every value from -3 onward
#IMPORTANT EXAMPLE
#this prints ['second', 'third', 'fourth']
print(my_list[:])
#this copies the list
print(my_list[0:4:2])
#this moves 2 elements forward every time
#so 0, 2, and NOT 4 are printed
#so ['first', 'third']
print(my_list[::-1])
#this REVERSES A LIST
#step value is -1

a = [1,2,3,4]
b = a
#this means that if you change a, you AUTOMATICALLY CHANGE B, since they are pointing to the same list
c = a[:]
#this is a copy of the list, so c is pointing to only a COPY of list a
#so changes to list a will not change c

my_list = [23, 45, 66, 69]
my_list[0] = 100
#this assigns 100 to the first index
print(my_list)
#my_list[0:2] = 100
#print(my_list)
#this results in an error because the left is a slice that is iteratable
#and the number on the right is not iteratable
#if we want to make it iteratable, we need to make it a list with brackets
#IMPORTANT EXAMPLE
my_list = [23, 45, 66, 69]
my_list[0:2] = [100]
#this will JUST print [100, 66, 69]
#NOTE HOW this just replaces indexes 0 and 1 because 2 is excluded from range
#IT DOES NOT PRINT 2 100s!!!!!
#IMPORTANT EXAMPLE
print(my_list)
my_list = [23, 45, 66, 69]
my_list[0:2] = [100, 200, 300]
print(my_list)
#now this will print IN PLACE OF 0-1 (bc 2 excluded from range), [100, 200, 300] THEN print
#the remaining values of 2, 3 as NORMAL
#so this will print [100, 200, 300, 66, 69]
#IMPORTANT EXAMPLE
#my_list[0:4:2] = [100, 200, 300]
#this is an issue because we are trying to assign a sequence of 3 ELEMENTS to a slice of 2 elements
my_list = [23, 45, 66, 69]
my_list[0:4:2] = [100, 200]
#this replaces index 0 with 100 and index 2 with 200
print(my_list)
#this should print [100, 45, 200, 69]

#my_list = [23, 45, 66, 69]
#my_list[0:4:2] = [100]
#this does NOT work because you are assigning a sequence of 1 to a slice of size 2
#whenever you are changing exact positions and not an entire chunk, you need the same number
#IMPORTANT EXAMPLE
#print(my_list)

a = [1,2,3,4]
b = [5,6]
c = a + b
print(c)
#this will output [1,2,3,4,5,6]
#so like concatenating the lists???
print(a,b)
#this will print [1,2,3,4] [5,6]
#so like the lists, but separated

my_list = [1,2,3,4,5]
my_list[1:3] = [100]
#this sets 1-2, EXCLUDING index 3 which are 2,3 to 100
print(my_list)
#this prints 1, 100, 4, 5
#DON'T MESS UP THE RANGE PLS
#IMPORTANT EXAMPLE YOU MISSED IT FIRST TIME

my_list[1:3] = "hello"
print(my_list)
#again, note how 1:3 will only change 1,2
#so right now that will change 100, 4
#IMPORTANT EXAMPLE WTF
#this will print
#[1, 'h', 'e','l','l','o',5]
#wtf, i hate this

my_list[1:6] = (2,3,4)
#a tuple is not like a list because it is immutable
print(my_list)
#this changes 1,2,3,4,5 indexes to 2,3,4
#so it will print [1, 2, 3, 4, 5]
#IMPORTANT EXAMPLE

my_list[1:3] = [] #this removes elements from 1 and 2
#so 1 and 2 are currently 2 and 3
print(my_list)
#so this prints [1, 4, 5]

my_list = [1,2,3,4,5]
my_list.append(6) #appends a single element
my_list.extend([7,8,9]) #this adds multiple elements
print(my_list)

my_list.insert(3,99) #this inserts 99 at index 3
print(my_list)
#oml why is he jamming all of this in one lecture

my_list.remove(99) #this will remove 99
#AND IF THERE ARE MULTIPLE 99s, it will remove only the FIRST ONE
print(my_list)

my_list.pop(0)
print(my_list)
#this removes the element at index 0

my_list = [5,2,1,4,3,3,9]
my_list.sort()
print(my_list)
#this sorts a list from least to greatest

my_list.reverse()
print(my_list)
#this reverses the list

my_list.clear()
print(my_list)
#this prints [0]


a = [1,2,3,4]
b = [5,6]
c = a + b
a.extend(b)
#this adds the multiple values of b to the list a
print(a,b)
#this should print [1,2,3,4,5,6], [5,6]
d = [6] * 10
print(d)
#this will print [6,6,6,6,6,6,6,6,6,6,]


#now NESTED LISTS
first_list = [[22, 33, 44], [55,66,77], [88,99,100]]
print(first_list)
print(first_list[0]) #will print [22,33,44]
print(first_list[0][1])
#this narrows it down to the first list, then goes to the 1st index of 33
#so it will print 33

res = []
for sublist in first_list:
    res.append(sum(sublist))
print(res)
#we create a blank list and want it to be the sum of each of the lists in first_list
#so 1 by 1, sublist will start with [22,33,44], take the sum, and append it to res
#then it gets [55,66,77], sums it, and adds it to the list
#then it gets [88,99,100], sums it, and adds it to the list
#so it prints [99,198,287] as res

res2 = [sum(sublist) for sublist in first_list]
#so this iterates over first list, continuously does the sum of it, and adds those values to a new list
#so this gives the same result as what we just did above

#print the list of even numbers from 0 to 9
res = []
for i in range(0, 10):
    if i%2 == 0:
        res.append(i)
print(res)

res2 = [i for i in range(0,10) if i%2 ==0]
print(res2)
#KNOW THIS FORMAT TOO!!!!!!! i bet he'll screw you over with this on the exam

#two dimensional lists
mat = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
#this could be used for games like tic-tac-toe

num_rows, num_cols = 3,4
board = []
#blank board
for i in range(num_rows):
    row = []
    #3 rows that you fill 1 by 1
    for j in range(num_cols):
        row.append("-")
        #once the row is filled up, we want to attach it to the board
    board.append(row)
    #3 rows with 4 dashes in each one
print(board)

board2 = ["-" for j in range(num_cols) for i in range (num_rows)]
print(board2)
#what the hell

my_list = [[1,2,3], [4,5,6], [7,8,9]]

print(my_list[0][0], my_list[0][1], my_list[0][2])
print(my_list[1][0], my_list[1][1], my_list[1][2])
print(my_list[2][0], my_list[2][1], my_list[2][2])

print()
for ls in my_list:
    #for sublist in my_list
    for item in ls:
        #for item in sublist, it prints the item with a space in between
        print(item, end=' ')
    print()
    #then after each sublist, it prints a new line
    #so this is equivalent to the 3 lines above

rows, cols = (3, 4)
board = [["-" for i in range(cols)]  for j in range(rows)]
board[0][1] = 'x'

for row in board:
    print(row)


print()
#this example is equivalent
board = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append("-")
    board.append(row)


board[0][1] = 'x'

for row in board:
    print(row)

#list comprehension to provide shorter syntax to create a new list by iterating over another iterable and modifying each element
first_list = [[1,2,3], [4,5,6], [7,8,9]]
sum_sublists = [sum(sublist) for sublist in first_list]
print(sum_sublists)

def square(x):
    return x*x
second_list = [3,5,8,2]
square_elements = [square(item) for item in second_list]
print(square_elements)

even_numbers = [i for i in range(0, 10) if i % 2 == 0]
print(even_numbers)


#WOOCLAP
my_list = [1,2,3,4]
my_list.extend([2,3,6])
my_list.append(100)
my_list.pop(0)
print(sum(my_list))

#so this adds 1,2,3,4,2,3,6
#then this appends 100
#1,2,3,4,2,3,6,100
#then this removes the index 0??????
#then the remaining sum is 120

#KMS <3
board = [[1,2,3], [4,5,6]]
print(board[1][2] + board[0][1])
#this would be
#um
#6 + 2
#so um
#like
#GOT WRONG
#6 + 2 = 8

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