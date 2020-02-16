num = []
num.append(int(input()))
num.append(int(input()))
num.append(int(input()))
num.append(int(input()))
num.append(int(input()))

y = 0
for x in num:
           if x%2 == 0:
                y += 1

print("%d valores pares"%y)