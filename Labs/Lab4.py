def fibonacci(n):
    a, b = 0, 1
    #Have to initialize these INSIDE the code otherwise it will give you an error
    #You also want to reset these every time the function runs, so this makes sense
    if n == 1:
        return(0)
    elif n == 2:
        return(1)
    else:
        for i in range(2, n):
            a, b = b, a + b
            #Have to update these at the same time or else the wrong values will be added!
        return(b)

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            #We have to start at 2 because we just said n has to be greater than 1
            if n % i == 0:
                return False
        return True
        #Once return is stated, then the whole function and loop will STOP RUNNING!

def print_prime_factors(n):
    if is_prime(n) == True:
        print(f"{n} = {n}")
    else:
        print(f"{n} = ", end = "")
        while n % 2 == 0:
            print(2, end="")  # Print factor 2
            n = n//2
            #So like if 24 is divisible, it'll print 2 then divide n to 12, then if there's still
            #and n value greater than 1, we'll print a star because there are more factors
            if n > 1:
                print(" * ", end="")  #Have to put the end so it doesn't start a new line
            #So now we go all the way down to n = 3, and n is no longer divisible, so
            #we'll start checking factors other than 2
        factor = 3
        while factor <= n:  #Have to put this here or else when 3 fails for a number like 10, it will just add
            #the factor and make it 5, but move on unless there is a greater loop that makes it check n % factor again
            while n % factor == 0:
                print(factor, end="")
                n = n//factor
                if n > 1:
                    print(" * ", end="")
            factor += 2
            #Go to the next odd number
        print()  # Move to the next line after all factors are printed


