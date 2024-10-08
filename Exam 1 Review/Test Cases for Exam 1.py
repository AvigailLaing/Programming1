val = 1

for i in range(-10, 1):
    for j in range(2, 6):
        val *= j
        break

print(val)

print("\nWow {this is interesting} [wow]")

def concat_words(word, repeats):
    result = word + " "
    for i in range(repeats - 1):
        if i != 0:
            result += " "
        result += word
    return result

print("\n" + concat_words("hello", 3))

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

print("\nThe integer function on 3.87 produces " + str(int(3.87)))
print("The round function on 3.87 produces " + str(round(3.87)))

number = input("\nEnter a number to reverse: ")
reversed_number = number[::-1]
print(reversed_number)

number = input("\nEnter a number to reverse: ")
reversed_number = ""
for i in range(len(number) - 1, -1, -1):
    reversed_number += number[i]
print(reversed_number)