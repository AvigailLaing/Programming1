#QUESTION 2
#Create a program that returns the least amount of bills needed to pay
#Using 1, 5, and 10 dollar bills
#Cost 15:
#see if 10 divides into it
# bills = 0
# cost = int(input("Cost: "))
# if cost < 5:
#     bills = cost
# elif cost == 5:
#     bills = 1
# elif (cost > 5 and cost < 10):
#     bills += 1
#     bills += (cost - 5)
# elif cost == 10:
#     bills = 1
# elif cost > 10:
#     if cost <= 14:
#         bills = 1 + (cost - 10)
#     else: #for 15-19
#         bills = 1 + 1 + (cost - 15)
#
# print(f"Minimum amount of bills required = {bills}")
#
# #QUESTION 3
# import random
# target_number = random.randint(1,10)
# user_guess = int(input("\nGuess a number between 1 and 10: "))
# if user_guess < target_number:
#     print("Too low!")
# elif user_guess > target_number:
#     print("Too high!")
# else:
#     print("Congratulations! You guessed the correct number!")
#
# #QUESTION 4
# grantTotal = float(input("\nWhat is the total grant amount for the field trip? "))
# edPrograms = int(input("How many educational programs are you planning to attend? "))
# anFed = int(input("How many animal feeding sessions are you planning to attend? "))
# guidTours = int(input("How many guided tours are you planning to organize? "))
# souv = int(input("How many souvenirs are you planning to purchase? "))
# vouch = int(input("How many lunch vouchers are you planning to buy? "))
#
# print("\nThe cost of each value is as follows: ")
# print("\nEducational Program: $20.50")
# print("Animal Feeding Session: $15.75")
# print("Guided Tour: $30.00")
# print("Souvenir: $10.25")
# print("Lunch Voucher: $12.00")
#
# #Now calculate total cost and if it is above or below grant amount, and by how much
# cost = (edPrograms * 20.50) + (anFed * 15.75) + (guidTours * 30.00) + (souv * 10.25) + (vouch * 12)
# difference = grantTotal - cost
#
# if difference >= 0:
#     print(f"\nYou are within the grant! You have ${difference:.2f} remaining.")
#     #Here, use the 2f formatting so it always shows 2 decimal places
# else:
#     print(f"\nYou are over the grand limit! You need an additional ${abs(difference):.2f}.")
#     #Be careful with syntax here

#QUESTION 5
#Pick the better plan
hours = int(input("How many hours? "))
basicPlanSum = 0
premiumPlanSum = 7
#Remember
if hours <= 5:
    basicPlanSum += (10 * hours)
    premiumPlanSum += (9 * hours)
if hours > 5 and hours < 11:
    basicPlanSum += 50
    premiumPlanSum += 45
    basicPlanSum += (hours - 5) * 15
    premiumPlanSum += (hours - 5) * 14
if hours > 10:
    basicPlanSum += 50 + (5 * 15)
    premiumPlanSum += 45 + (5 * 14)
    basicPlanSum += (hours - 10) * 20
    premiumPlanSum += (hours - 10) * 18

if basicPlanSum > premiumPlanSum:
    print("Plan: Premium")
    print(f"Cost: ${premiumPlanSum}")
    print(f"Savings: ${basicPlanSum - premiumPlanSum}")
elif premiumPlanSum > basicPlanSum:
    print("Plan: Basic")
    print(f"Cost: ${basicPlanSum}")
    print(f"Savings: ${premiumPlanSum - basicPlanSum}")
else:
    print("Plan: Basic")
    print(f"Cost: ${basicPlanSum}")
    print("Savings: $0")