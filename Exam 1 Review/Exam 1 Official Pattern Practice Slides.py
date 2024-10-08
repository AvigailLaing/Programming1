#PROBLEM 1
#*   *
#** **
#*****
#** **
#*   *

#*    *
#**  **
#******
#******
#**  **
#*    *

#We are going to have an i loop with an increasing astrix triangle, decreasing space triangle,
#ANOTHER DECREASING SPACE TRIANGLE, and increasing astrix triangle
#Then we will have another i loop with a decreasing astrix triangle, increasing space triangle,
#ANOTHER increasing space triangle, and a decreasing astrix triangle

n = 3
for i in range(1, n):
    #This creates 3 rows
    for j in range(i):
        #i = 1, 0-1, 0, 1 star will be printed
        print("*", end = "")
    for j in range(i, n):
        print(" ", end = "")
        #i = 1, n = 3, 1, 2
        #This should print two spaces for i = 1
    for j in range(i, n):
        print(" ", end = "")
        #This should print 2 more spaces
    for j in range(i):
        print("*", end = "")
        #This will print 1 star
    print()
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print("*", end = "")
        #This should print 3 stars
    for j in range(i - 1):
        print(" ", end = "")
        #This should print 0 spaces
    for j in range(i - 1):
        print(" ", end = "")
        #This should also print 0 spaces
    for j in range(i, n + 1):
        print("*", end = "")
        #This should print 3 more stars
    print()
    #NOW WE HAVE AN EXTRA ROW, SO ALL WE DO IS ADJUST THE RANGE ON ONE OF THE I LOOPS TO (1, n)
    #FOR SOME REASON ONLY THE FIRST I LOOP IS A GOOD IDEA FOR THIS
print()

#INCREASING TRIANGLE
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end = "")
    print()

print()

#DECREASING TRIANGLE
n = 5
for i in range (1, n + 1):
    for j in range(i, n + 1):
        print("*", end = "")
    print()

print()
#DECREASING TRIANGLE OF SPACES THEN INCREASING TRIANGLE OF ASTRICES
#Row 1 should have ____*
#Row 2 shuold have ___**
n = 5
for i in range(1, n + 1):
    #this gives us the correct number of rows
    for j in range(i, n):
        #only n this time since we need to save one spot for the astrix
        print(" ", end = "")
    for j in range(i):
        print("*", end = "")
        #so right after ____ prints, this prints the number of astrices in the row
    print()
    #now this creates a new line

#INCREASING TRIANGLE OF SPACES THEN DECREASING TRIANGLE OF ASTRICES
#Row 1 should have *****
#Row 2 should have  ****
n = 5
for i in range(1, n + 1):
    #START WITH INCREASING TRIANGLE OF SPACES
    for j in range(i - 1):
        #So for i = 1, it won't run and print anything
        #For i = 2, it will print once
        #For i = 3, range will be (2), so j = 0 and j = 1, meaning it runs twice
        print(" ", end = "")
    for j in range(i, n + 1):
        print("*", end = "")
    print()

print()
#HILL, NOTE WE NEED ONE LESS COLUMN SO WE HAVE A PEAK
n = 5
for i in range(1, n + 1):
    for j in range(i, n):
        print(" ", end = "")
    for j in range(i - 1):
        #TAKE ONE COLUMN AWAY
        print("*", end = "")
    for j in range(i):
        print("*", end = "")
    print()

print()
#REVERSE HILL
#Increasing space, decreasing star, decreasing star
n = 5
for i in range(1, n + 1):
    for j in range(i - 1):
        print(" ", end = "")
    for j in range(i, n + 1):
        print("*", end = "")
    for j in range(i, n):
        print("*", end = "")
    print()

print()

#SQUARE PROGRAM!!!
for i in range(1, n + 1):
    for j in range (1, n + 1):
        print("*", end = "")
    print()

def repeatMenu():
    number = input("Enter a number: ")
    return number
number = repeatMenu()
input_list = []
#have to do this or else the number variable won't be set right
while number != "999":
    input_list.append(number)
    #now set number = result of menu function
    number = repeatMenu()
print("Your input: " + ", ".join(input_list))