#print pattern with
#*       *
#* *   * *
#* * * * *
#* *   * *
#*       *

#i is row, j is column
#so first we want 1,1 printed then 1,5
#then 2,1 2,2 and 2,4 2,5
#then 3,1 3,2 3,3 3,4 3,5
#then 4,1 4,2 and 4,4 4,5
#then 5,1 and 5,5

#two diagonals
#all values in one diagonal add to 6
#for the right side, i + j == n + 1
#on right side of diagonal, i + j > n + 1
#on the left side of the diagonal, i + j < n + 1
# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i + j >= n + 1:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
#This is for the first diagonal

#on the second diagonal, i == j
#and on the left side of that diagonal, i > j
#we want that triangle, so only when i > j  and i + j < n + 1

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i >= j and i + j <= n + 1) or (i <= j and i + j >= n + 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#whenever we don't know the number of terms, we use a while loop
n = int(input("Enter a number: "))
def is_prime(n):
	if n > 1:
		for i in range (2, n):
			if n % i == 0:
				print(f"{n} is not prime")
				break
		#we need this indented OUT because otherwise as soon as it
        #isn't divisible by a number it'll say its prime without
        #checking all the numbers leading up to it!!!
		else:
				print(f"{n} is prime")
	else:
	    print(f"{n} is not prime")

is_prime(n)

