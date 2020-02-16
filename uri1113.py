while True:
    try:
        x,y = list(map(int,input().split()))
        if(x==y):
            break
        else:
            if x>y:
                print("Decrescente")
            elif x<y:
                print("Crescente")
    
    except:
        break