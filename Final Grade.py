#Write a program to calculate the final grade of the course

import math
a = math.pow(3,2)
print(a)

num = 6.7
b = math.ceil(num)
print(b)
#Rounds up to the next number, even if you put 6.3 it will round up to 7
c = math.floor(num)
print(c)
#Floor always rounds down to the next number, even if you put 6.7 it will round to 6
d = math.sqrt(num)
print(d)

quiz_score = float(input("Enter the average quiz score: "))
lab_score = float(input("Enter the average lab score: "))
exam_score = float(input("Enter the average exam score: "))
project_score = float(input("Enter the average project score: "))
final_grade = quiz_score*.15 + lab_score*.25 + exam_score*.4 + project_score*.2
print(f"The final grade is {final_grade:.2f}")

# a = 20
# b = 5
# c = 4
# x = b+a/b*c+c-b
#First do a/b, so 20/5, then multiply by c = 4 * 4 = 16
#b + 16 = 21 + 4 - 5 = 20
#25/20
25/20 + 4 - 5

