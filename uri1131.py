i = 1
v = 0
m = 0
n = 0
z = 0
while i<2 and i>0:
    x,y = list(map(int,input().split()))
    print("Novo grenal (1-sim 2-nao)")
    i = int(input())
    v += 1
    if x>y:
        m += 1
    elif y>x:
        n += 1
    elif y==x:
        z += 1


print("%d grenais" %v)
print("Inter:%d" %m)
print("Gremio:%d" %n)
print("Empates:%d" %z)

if m>n:
    print("Inter venceu mais")
elif n>m:
    print("Gremio venceu mais")
elif m == n:
    print("Não houve vencedor")


