n = int(input())
x = 1
if n>2 and n<1000:
    while x<=10:
        t=x*n
        print("%d x %d = %d" %(x ,n ,t))
        x += 1