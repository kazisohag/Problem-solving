s = 0
i = 1
while i <= 2:
    x = float(input())
    if(x >= 0 and x <= 10):
        s += x
        i += 1
    else:
        print("nota invalida")

print("media = %.2f" %(s/2))