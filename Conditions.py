#Conditionals

total = float(input("Enter the final grade: "))
print(total)

if total > 90:
    print("Satisfactory performance.")
elif total > 80:
    print("B grade.")
elif total > 70 and total < 79: #70 < total < 79
    print("C grade.")
else:
    #Else is a clause, it does not have a condition
    print("Work harder, all the best!")
    #If and else are keywords in Python

#Write a program to calculate the final price which the customer has to pay
#if the store has the deal "Buy 3, pay for the costliest 1."
#We need to figure out how to calculate the costliest one.
#Person puts 3 inputs of the 3 costs, then it decides which one is bigger

c1 = float(input("Enter the cost of item 1: "))
c2 = float(input("Enter the cost of item 2: "))
c3 = float(input("Enter the cost of item 3: "))
if c1 >= c2 and c1>=c3:
    print(c1)
elif c2 >= c1 and c2 >= c3:
    print(c2)
elif c3 >= c1 and c3 >= c2:
    print(c3)
#Maybe add what to do if two items are equal