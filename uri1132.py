x = int(input())
y = int(input())
s = 0

if x<y:
    for v in range(x,y+1):
        if (v%13)!= 0:
            s += v
elif y<x:
    for v in range(y,x+1):
        if (v%13)!= 0:
            s += v


print(s)
