N = int(input())
x = []

y = 0
i = 0

for i in range(N):
    x.append(input())
for y in x:
    if int(y)>0:
        if int(y)%2 !=0:
            print("ODD POSITIVE")
        elif int(y)%2 == 0:
            print("EVEN POSITIVE")
    
    if int(y)<0:
        if int(y)%2 !=0:
            print("ODD NEGATIVE")
        elif int(y)%2 == 0:
            print("EVEN NEGATIVE")

    if int(y) == 0:
        print("NULL")