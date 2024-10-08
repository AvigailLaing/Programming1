print(f"You like too? I love [song]")
num = 13//10
num2 = round((num * 16) / 5)
print(num2)

a = 10
b = 20
c = 30
if a!= b and b == c:
    print("This true")
elif not (a !=b and b != c):
    print("No, true")
elif a == b or b!=c:
    print("Are you sure?")
else:
    print("All of above false")
def calculate(b):
    b = b*2 + 25
    print("Calculated!")
x = 7
print(calculate(x))

def min_value(x,y):
    return x if x < y else y
print(min_value(1131, 1311))

x = 0
y = 8
while x < y:
    y -=1
    x = y//2
    if x % 2 != 0:
        x += 1
print(x)

val = 2
for i in range(-5, 6, 2):
    for j in range(3,5):
        val *= j
    break
print(val)

def print_output(function, *args):
    value = 5
    for arg in args:
        value += arg
    print(f"{function(value)}")
def magic(x):
    return int(x**0.5)
print_output(magic, 7, 4, 2, 2, 5)

x = 0
for i in range(5):
    while i > 0:
        x += i
        i -= 2
print(x)

def old(x, y, z):
    value = x(y,z)
    print(value)
def new(a, b):
    return (a + b) * 2 + 23
old(new, 2, 3)

def add_five(n):
    return n + 5
def subtract_three(n):
    return n - 3
p = subtract_three
q = add_five
r = p
s = lambda n: n * 4
r = s
print(p(8) + q(7) + r(2))

def collatz_sequence(n):
    if n > 0:
        print(n)
        while n!= 1:
            if n % 2 ==0:
                n = n/2
            else:
                n = (n*3) + 1
            print(n)
collatz_sequence(3)

def nth_narayana(n):
    a = 1
    b = 1
    c = 1
    for i in range(0, n - 3):
        #I put n -2 RIP
        a, b, c = b, c, a + c
    print(c)
nth_narayana(4)