n = int(input())
i = 1
while i<=n:
    x,y = list(map(int,input().split()))
    x = float(x)
    y = float(y)
    if y == 0:
        print("divisao impossivel")
    else:
        z = x/y
        print("%.1f" %z)

    i += 1