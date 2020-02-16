a = []
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))

y = 0
t = 0.0

for x in a:
    if(x>0):
        y += 1
        t += x

av = t / float(y)
print("%d valores positivos" %y)
print("%.1f" %av)
