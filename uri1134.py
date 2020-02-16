i = 1
s = 0
y = 0
z = 0
n = 2

while i<=n:
    x = int(input())
    if x<4:
        if x == 1:
            s += 1
            
        elif x == 2:
            y += 1
            
        elif x == 3:
            z += 1
    elif x == 4:
        i = n+1
    
    i += 1
    n += 1


print("MUITO OBRIGADO")
print("Alcool: %d" %s)
print("Gasolina: %d" %y)
print("Diesel: %d" %z)