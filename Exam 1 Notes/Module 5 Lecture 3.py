#modifying lists is mutable

def team(name, project):
    print(name, "is working on", project)
team("David", "Blackjack")
#THESE ARE POSITIONAL ARGUMENTS

#but you can also do keyword arguments by name rather than position
team(name = "David", project = "Blackjack")
#THIS IS A KEYWORD ARGUMENT
team(project = "Blackjack", name = "David")

#can be mixed with positional arguments, but keyword arguments
#should come last
# team(project = "Blackjack", "David") WILL NOT WORK
#IT MUST BE:
team("David", project="Blackjack")

def team(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f'{key}:{value}', end="")
    print()

team("Sally", "Tom", project="Blackjack",group_num=2)

#can make add.py file
#a,b = 2,4
#print(a + b)

#then in subtract.py file
#from add import a,b
#print(b-a)
#it will print both the result of adding a + b and the new print statement!

#can do like import add
#print(add.b - add.a)

#__main__ is the main top level code you are running
#if you import from another python file, that python file's __name__ is
#just the name of the imported python fail