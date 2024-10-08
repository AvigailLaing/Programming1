totalIncome = float(input("Enter your total income this year: "))

if totalIncome <= 11000:
    owed_taxes = totalIncome * 0.10
elif totalIncome <= 44725:
    owed_taxes = (11000 * 0.10) + ((totalIncome - 11000) * 0.12)
    #First tax the full 11,000 bracket then tax everything between the top portion of the bracket and full income
elif totalIncome <= 95375:
    owed_taxes = (11000 * 0.10) + (33725 * 0.12) + ((totalIncome - 44725) * 0.22)
elif totalIncome <= 182100:
    owed_taxes = (11000 * 0.10) + (33725 * 0.12) + (50650 * 0.22) + ((totalIncome - 95375) * 0.24)
elif totalIncome <= 231250:
    owed_taxes = (11000 * 0.10) + (33725 * 0.12) + (50650 * 0.22) + (86725 * 0.24) + ((totalIncome - 182100) * 0.32)
elif totalIncome <= 578125:
    owed_taxes = (11000 * 0.10) + (33725 * 0.12) + (50650 * 0.22) + (86725 * 0.24) + (49150 * 0.32) + ((totalIncome - 231250) * 0.35)
else:
    owed_taxes = (11000 * 0.10) + (33725 * 0.12) + (50650 * 0.22) + (86725 * 0.24) + (49150 * 0.32) + (346875 * 0.35) + ((totalIncome - 578125) * 0.37)

print(f"You owe ${owed_taxes:.2f} this year.")
