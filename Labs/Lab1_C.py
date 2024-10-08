year1 = int(input("Enter the year for date 1: "))
month1 = int(input("Enter the month for date 1: "))
day1 = int(input("Enter the day for date 1: "))
year2 = int(input("Enter the year for date 2: "))
month2 = int(input("Enter the month for date 2: "))
day2 = int(input("Enter the day for date 2: "))

date1Total = (year1 * 360) + ((month1 - 1) * 30) + day1
date2Total = (year2 * 360) + ((month2 - 1) * 30) + day2
totalDif = abs(date2Total - date1Total)
print(f"The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {totalDif} days!")
