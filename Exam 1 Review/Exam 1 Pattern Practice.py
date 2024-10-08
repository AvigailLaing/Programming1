#RIGHT TRIANGLE PROGRAM
base = int(input("Enter base size: "))

for i in range(1, base + 1):
    #Each iteration of this loop creates a new row
    #First time it prints 1 star
    #Then 2 stars
    #Then 3 stars
    #Up until "base" stars is printed
    print("*" * i)

print("\n")
#SQUARE PROGRAM
# for i in range(base):
#     print()
#     #This creates a new line every time the loop runs, so we know we'll create "base" rows
#     for j in range(base): #start at 0, end at base
#         print("*", end = "") #have to put end statement so that astrices print 4 on same line
#         #This fills in the rows with "base" astrices on each row

#SQUARE PROGRAM!!!
for i in range(1, base + 1):
    for j in range (1, base + 1):
        print("*", end = "")
    print()
