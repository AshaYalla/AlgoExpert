def hasSingleCycle(array):
    i = 0 
    k = 0 
    n = len(array)
    while( k < n):
        i =( i +  array[i] ) %n
        k+=1
        if i == 0:
            break
    if i == 0 and k == n:
        return True
    return False