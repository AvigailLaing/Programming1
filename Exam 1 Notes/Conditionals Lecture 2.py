#Conditionals

count = 300000000
type = "Veg"

if (type == "Veg" or type == "Sup") and (count == 3 or count == 2):
    #Without the parantheses, it will print "Yes" even if the number is super high
    print("Yes")
    #And has a higher precedence than or, so it naturally goes
    #type == Veg or (type == "Sup" and count ==3) or count ==2

# total = float(input("Enter the grade: "))
# if total > 70:
#     if total > 90:
#         if total >= 98:
#             print("Is this even possible?")
#         else:
#             print("Great job!")
#     else:
#         print("Satisfactory performance.")
# else:
#     print("Work hard next time!")

# year = int(input("Enter the year: "))
#
# if year%4==0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("Leap Year")
#         else:
#             print("Not a Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Not a Leap Year")

# x = 5
# y = 6
# print("Yes") if x==y else print("No")

# x = 5
# y = 8
# if y<x:
#     x = x + 2
#     y = y - 2
# x = x + 1
# y = y + 1
#Use debug mode and step in with this


x = 1
#Initialization of variable

while x <= 100:
    print(x)
    x += 1
