x = int(input())
a = 1
b = 1
c = 1

for i in range(x):
    x = a
    y = b+1
    z = c+1
    print("%d %d %d" %(a,b,c))
    print("%d %d %d" %(x,y,z))
    a += 1
    b = a*a
    c = a*a*a

    