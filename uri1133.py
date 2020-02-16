x = int(input())
y = int(input())
s = 1

if x<y:
    for v in range(x+1,y):
        if (v%5)== 2 or (v%5)==3:
            print(v)
elif y<x:
    for v in range(y+1,x):
        if (v%5)== 2 or (v%5)==3:
            print(v)



