x = int(input())
y = int(input())

t = 0
for z in range (y+1,x):
    if z%2 != 0:
        t += z
print(t)
