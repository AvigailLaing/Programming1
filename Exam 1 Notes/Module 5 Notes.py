def say_hello(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

say_hello("Bob", 2)
#Don't forget the quotes around this

def increment(x):
    x+=1
    return x
    #instead of print(x)
    #but this means we need to use a print statement with increment(y)
y = 4

print(increment(y))
#x takes the value of 4
#if both the increment definition and here had print(x) and print(increment(y))
#the print(increment(y)) will print "None"

def increment(x):
    x+=1
    print(x)
    #this prints 5
y = 4
print(increment(y))
#this prints "None" because the function increment(x) doesn't return a value!!!



def palm_tree(x, y, z):
    a = y + z
    z = x
    y = z
    print(a + y + z)

palm_tree(2,3,4)

def palm_tree(x,y,z):
    a = y + z
    z = x
    y = z
    return a + y
#a = 3, z = 1, y = 1, return 3 + 1 = 4 = value, print(4 + 5) = 9
value = palm_tree(1, 1,2)
#doesn't work if you just do palm_tree(1) because it needs the other 2 parameters
print(value + 5)

def my_add(x,y):
    x = y
    return
    return x + y
#x = 3
#as soon as the first return hits, the execution stops
#but it isn't returning anything specific so it returns "None"
print(my_add(2,3))

def even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"
    #the first return is "Even" since the if condition is true,
    #so it only returns that
    #if the if condition wasn't met, it would return "Odd"

print(even_odd(240))