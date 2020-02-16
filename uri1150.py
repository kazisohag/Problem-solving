X = int(input())
Z = int(input())
i = 0

while Z<=X:
    Z = int(input())

y = X
while Z>y:
    y += X
    i += 1
    X += 1

print(i+1)
