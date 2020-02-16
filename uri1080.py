a = 0
x = {}
y = 0
while y < 100:
    z = int(input())
    if(z > a):
        a = z
        x[z] = y
    y += 1
print(a)
print(x[a]+1)