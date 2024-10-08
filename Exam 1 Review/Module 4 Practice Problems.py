x = 5

while True:
    #True is logical 1, false is logical 0
    #This means that True will always be running
    #It doesn't print anything because it keeps going back to
    #while True x+= 5
    #we need to actually make it stop or else it will always go
    x += 5
    if x<3:
        print('*')

print('*')


x = 5

while True:
    x+=5
    if x<8:
        print('*')
        break
print('*')
#Again, nothing will be printed
#The break statement we won't get to


x = 5

while True:
    x+=5
    if x<8:
        print('*')
    break
print(x)
#It will run once, make x 10, then print 10

var = 1
for i in range (3, 10, 3):
    var +=i
    print(var, end='')
#i starts with 3, 3 added to 1
#then it will print 4, then i will go to 6, 4 + 6 = 10, print 10
#then i will go to 9, 9 + 10 = 19, then it will print 19 and stop running
#prints 41019

var = 1
for i in range (10,5,-3):
    var += i
    print(var, end='')
#i starts with 10, 1 + 10 = 11
#11 printed
#i goes to 7, 11 + 7 = 18
#i can't go to 4 i think because that's not in the range
#so it just prints 1118

var = 1
for i in range(1, 5, -3):
    var += i
    print(var, end='')
print(var)
#BECAUSE THE RANGE IS INVALID, IT WON'T RUN, NOT EVEN ONCE!!!!!!
#i would eventually go -3, which is not in the range
#no number will be generated in the range
#THE FOR LOOP WILL NOT RUN
#so the value of var = 1 will be printed
