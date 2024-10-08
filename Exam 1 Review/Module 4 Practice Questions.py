#QUESTION 1
#Right Triangle Program

base = int(input("Enter base size: "))

for i in range(1, base + 1):
    print("*" * i)

#QUESTION 2
#Check whether a number is a palindromic number

number = input("\nEnter a number: ")
def is_palindrome(number):
    reversed_number = number[::-1] #works since number is a string
    if reversed_number == number:
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

is_palindrome(number)

number = input("\nEnter a number: ")
def is_palindrome(number):
    reversed_number = ""
    for i in range(len(number) - 1, -1, -1):
        reversed_number += number[i]
    if reversed_number == number:
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

is_palindrome(number)
# number = int(input("\nEnter the number: "))
# reversed_num = 0
# original_num = number
# while number > 0:
#     #If you modulus 10, you'll get the last number
#     digit = number % 10
#     reversed_num = reversed_num * 10 + digit
#     number = number // 10
#
# if original_num == reversed_num:
#     print(f"{original_num} is a palindrome!")
# else:
#     print(f"{original_num} is not a palindrome.")

#QUESTION 3
#REVERSE A NUMBER
number = input("\nEnter a number to reverse: ")
reversed_number = number[::-1]
print(reversed_number)

number = input("\nEnter a number to reverse: ")
reversed_number = ""
for i in range(len(number) - 1, -1, -1):
    reversed_number += number[i]
print(reversed_number)

# number = int(input("\nEnter a number to reverse: "))
# original_number = number
# reversed_num = 0
# #must initialize variables
# #start by modulus 10 to get the last digit
# while number > 0:
#     digit = number % 10
#     reversed_num = reversed_num * 10 + digit
#     number = number // 10
# #now take the original number and divide by 10 so that you can move
# #onto getting the next digit and reversing it
#
# print(f"{original_number} reversed is {reversed_num}!")


#QUESTION 4
print()
def repeat():
    number = input("Enter a number: ")
    return number

number = repeat()
#HAVE to set number = repeat() instead of just running repeat()
input_list = []
while number != "999":
    #also, since our input for number is a string, we have to compare it to a string "999" instead of regular 999
    input_list.append(number)
    number = repeat()
    #also here have to set number = repeat() or else the number value won't make it back here!
print("Your input: " + ", ".join(input_list))
print()
#QUESTION 5, factorial program
number = int(input("Enter a positive integer: "))
original_number = number

for i in range(number - 1, 0, -1):
    number *= i
print(f"The factorial of {original_number} is {number}.")

#QUESTION 6, series question
number = int(input("\nEnter a positive non-zero integer: "))
series_sum = 0
for i in range (1, number + 1):
    inner_value = 0
    #because we have to reset the inner sum every time we reiterate the whole loop
    for j in range (1, (number * 2) + 1):
        inner_value += ((j**2)/2 - (j**3)/3)/j**3
    series_sum += i * inner_value
print(f"The value of the series for N = {number} is {series_sum}.")
