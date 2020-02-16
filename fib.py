fib = [0,1]
x = 0
y = 1

for x in range(60):
    x += y
    y += x

    fib.append(x)
    fib.append(y)
    if x >= 60:
        break

    

print(fib)
