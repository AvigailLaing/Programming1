str = "Python"
print(str[1:4])
#This will print 3 characters: yth
print(str[::-1]) #= reversed
#This is 0:end:-1, so it goes 0 to end, but in reverse

my_list = [23, 45, 67, 78]
print(my_list[1:3])
#This prints [45, 67]

#Remember that slices print with the brackets, but if you print a specific element
#from the list by referencing its index, it does NOT print with brackets
#This was something you initially missed on "Quiz 5"

my_list = [[23, 45, 67, 78], [45, 89], 56]
print(my_list[0])
print(my_list[0][2])
#This line will grab the first sublist, index 2, so it will print 67 without brackets
print(my_list[-2])
#This prints [45, 89] because negative index on the very right starts with -1

nested = [0]
original = [nested, 1]
print(original)
#The output will be 0 and 1 because nested refers to 0

nested[0] = 'zero'
print(original)
#This will print [['zero'], 1], but the 'zero' is in brackets because it is a list

original[0][0] = 2
#This says that the first sublist [nested] and the first element of it
#'zero' will become 2
#Printing the nested will now print [2]
print(nested)
print(original)
#And the original is now [[2], 1]

#THIS IS THE START OF NEW STUFF YOU'LL WANT TO COPY
#How do we create a deep copy where we can change the values in one variable without affecting the other?
import copy

original = [[0], 1]
shallow = original[:]
#Shallow is a copy of original, but Shallow's first element refers to the same 0 list as the original
deep = copy.deepcopy(original)
#This creates a copy of [[0], 1], but this time, the [0] list is a brand new one of its own

shallow[0][0] = 2
#Because the shallow copy points to the same sublist [0] as the original, we can change it
print(original, shallow)

deep[0][0] = 3
print(original, deep)
#Because deep points to a brand new [0] sublist of its own, this will not change the original

numbers = [1,2,3,4,5]
squared_numbers = [num**2 for num in numbers if num % 2 == 0]
print(squared_numbers)
#This will print 4 and 16
#You must know how to create these list loops on the fly
#Variable "num" will first be 1, then 2, then 3, then 4, then 5
#Then whichever num is even be squared

original_list = [1,2,3,4,5,6,7,8,9]
sliced_list = original_list[2:7]
#3-7 are the numbers that will be chosen
print(sum(sliced_list))
#This will print 3 + 4 + 5 + 6 + 7
#This will print 25 with no brackets

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

a = [1, 5] + [3]
#This would be [1,5,3]
a.append(1)
#[1,5,3,1]
a.extend([1,3])
#[1,5,3,1,1,3]
print(a)

b = [8,2,7,1,6,12]
c = [item//2 for item in b if item % 2==0]
c[0:-1] = '12'
print(c)
#If divisible by 2, it is divided by 2 and added to c
#c = [4, 1, 3, 6]
#Now c from index 0 to -1, so from 4, 1, 3 are set to '12'
#So this would be ['1','2', 6] , note how the string is split up
#Yessss, I got it right

a = [8] * 2
#This = [8,8]
b = [5,9,1]
c = [a,b]
#This = [[8,8], [5,9,1]]
#These point to the original a and b lists
d = c
#d = [[8,8], [5,9,1]]
#This points also
a[:] = [6]
#shallow copy of a equals [6]?
#This resets the entire list of a to 6
b[2] = 4
#Now 1 in b is changed to 4, so b is 5,9,4
print(d)
#D was referring to c, and c was referring to a and b
#Since we have fundamentally changed a and b, d has also been updated
#This will print [[6], [5,9,4]]

