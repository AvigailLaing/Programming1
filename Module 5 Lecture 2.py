from ast import increment_lineno
from lib2to3.pgen2.tokenize import double3prog

sum = lambda a,b: a + b
print(sum(1,2))
#anonymous function defined with lambda instead of def

def outer_func():
    square = lambda x: x**2
    print(square(5))
    #This prints out 25
outer_func()

num = 2
def magic(x):
    num = 5
    return num + x
print(magic(num))
#num = 2
#then we slap num = 2 into the function as x
#so then x = 2, but num = 5
#then it returns 2 + 5 = 7 (CORRECT)

num = 2
def magic(x):
    return num + x
print(magic(num))
#so we slap num = 2 into the function
#and it returns num = 2 + 2 = 4 (CORRECT)

a,b = 2,3
def magic():
    a = "two"
    b = "three"
print(a,b)
magic()
#as soon as the execution of agic ends, a and b's local values
# of "two" and "three" are negligible because there is no return
#so it goes back to being 2,3
print(a,b)

a,b = 2,3
def magic():
    global a
    a = "two"
    b = "three"
print(a,b)
magic()
#But using "global" in the function makes it so that the value of a
#sticks to "two" even after the function is done
print(a,b)
