s = 0
for i in range (2,8):
    if i ==3:
        continue
    if i ==6:
        break
    s = s + i
print(s)
#s = 0 + 2
#then it runs again, i = 3
#skips?
#i = 4, s = 4 + 2 = 6
#i = 5, s = s + i - 6 + 5 - 11
# now i = 6, so it breaks, s = s+ 1 isn't hit
#s is printed = 11