length1 = float(input("Side length 1: "))
length2 = float(input("Side length 2: "))
length3 = float(input("Side length 3: "))

if (length1 == length2) and (length2 == length3):
    print("This is an equilateral triangle!")
elif (length1 == length2) or (length2==length3) or (length1 == length3):
    print("This is an isosceles triangle!")
else:
    print("This is a scalene triangle!")