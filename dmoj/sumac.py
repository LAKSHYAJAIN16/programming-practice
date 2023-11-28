t1 = int(input())
t2 = int(input())

def sumac(t1, t2, it):
    t3 = t1-t2
    t4 = t2-t3
    if t4 < 0:
        return it + 1
    else:
        return sumac(t2, t3, it  + 1)
        
print(sumac(t1, t2, 2))