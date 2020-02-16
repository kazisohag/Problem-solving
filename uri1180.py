
x = int(input())
if x>1 and x<1000:
    l = list(input())

    if len(l)<=10:
        Mvalue = max(l)
        print("Menor valor: " ,Mvalue)

        ind = l.index(Mvalue)

        print("Posicao: ",ind)
           



