x = int(input())
a = 1
b = 1
c = 1

for i in range(x):
    print("%d %d %d" %(a,b,c))
    a += 1
    b = a*a
    c = a*a*a