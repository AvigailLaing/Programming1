#QUESTION 2, CURRENCY CONVERTER
print("Welcome to the Currency Converter!")
print()
a = 1
b = 2
c = 3
print(a, b, c, sep = "\n")


present_value = float(input("\nInitial savings amount: "))
interest_rate = (float(input("Annual interest rate: ")))/100
years = int(input("Number of years for savings: "))

def future_value(present_value, interest_rate, years):
    future_value = present_value * ((1 + interest_rate)**years)
    return round(future_value, 2)

print(f"Estimated future value: ${future_value(present_value, interest_rate, years)}")

#PROBLEM 6, PRINT ALL COMBINATIONS OF DICE ROLLS GIVEN SIDES ON EACH DICE
def roll(dice1, dice2):
    for i in range(1, dice1 + 1):
        for j in range(1, dice2 + 1):
            print("(", i, ",", j, ")", end = " ", sep = "")
        print()

roll(4,6)
