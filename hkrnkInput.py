numbers = input().split()
x, y = numbers
x = int(x)
y = int(y)
v = y-1
n = ""
while v >= x:
    if v<2:
        n += " + "+'x'+" + "+"1"
    if v==2:
        n += 'x**%d' %v
    if v>2:
        n += ('x**%d' %v) +" + "
    
    v -= 1

print (n)
    
