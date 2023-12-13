import math
n = int(input())

def is_prime(k):
    for n in range(2, math.ceil(math.pow(k, 1/2)) + 1):
        if k % n == 0:
            return False
    return True

outs = []
for m in range(n):
    k = int(input())
    
    # += 2 until we find a prime number
    found = False
    piv = k
    n = 0
    
    while found == False:
        if is_prime(piv) == True:
            found = True
            break
        else:
            if piv % 2 == 0:
                piv += 1
                n += 1
            else:
                piv += 2
                n += 2
        
    num_1 = piv
    num_2 = k - n
    outs.append([str(num_1), str(num_2)])
    
for out in outs:
    print(" ".join(out))