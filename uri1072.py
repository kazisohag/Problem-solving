x=int(input())
N=[]
w=0
a=0
for v in range (1,(x+1)):
    N.append(input())
for v in N:
    if (10<=int(v)<=20):
        w+=1
    elif (int(v)>20) or(int(v)<10):
        a+=1
print(w ,"in")
print(a ,"out")