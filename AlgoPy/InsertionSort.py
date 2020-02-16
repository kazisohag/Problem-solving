def InsertuonSort(my_list):
    for num in range(1,len(my_list)):
        element = my_list[num]
        pos = num
        while element < my_list[pos-1] and pos > 0:
            my_list[pos] = my_list[pos-1]
            pos -= 1
    
        my_list[pos] = element

A = [2,33,65,87,1,0,4,7,30,81,65,10,65]
InsertuonSort(A)

print(A)




