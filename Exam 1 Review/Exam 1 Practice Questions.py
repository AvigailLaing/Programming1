def print_triangle():
    base = int(input("Enter the base size: "))
    for i in range(1, base + 1):
        print("*" * i)

print_triangle()

def print_inverse_triangle(base):
    for i in range (base, 0, -1):
        print("*" * i)
base = int(input("Enter the base size: "))
print_inverse_triangle(base)

a = 6
b = 5

print(a, end=" ")
print(b)

def identica_digits(num):
    identicalDigits = [11, 22, 33, 44, 55, 66, 77, 88]
    while num >= 10 and num <=90:
        print(num, end = " ")
        if num in identicalDigits:
            break
        num += 1

num = int(input("num = "))
identica_digits(num)

sumList = []
stillGoing = True
while stillGoing == True:
    numSum = int(input())
    if numSum <= 0:
        stillGoing = False
        break
        #Have to add a break statement or it will keep moving into the loop because stillGoing was true when it started
    sum = 0
    #Need to move into this loop so it resets after each iteration!
    for i in range(1, numSum + 1):
        numAdd = int(input())
        sum += numAdd
    print(sum)

