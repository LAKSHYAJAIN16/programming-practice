def sol1(i : int):
    ans = 0
    for f in range(0, int(i / 4) + 1):
        x = (i - 5*f) % 4
        if x == 0:
            ans += 1      
    return ans

def sol2(j : int):
    f = []
    for g in range(0, int(j / 4) + 1):
        if (j - 5*g) % 4 == 0:
            f.append(j - 5*g)
            if len(f) == 2:
                return int(f[1] / 20) + 2
            
    if len(f) == 1:
        return 1
    
    return 0