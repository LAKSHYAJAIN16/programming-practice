n, m, k = list(map(int, input().split(" ")))

keys = {}
ar = []
for q in range(n):
    ar.append(q + 1)
    
for j in range(n):
    keys[str(j + 1)] = ar
print(keys)

for i in range(k):
    f = input().split(" ")
    if len(f) == 9:
        num1 = f[2]
        num2 = f[5]
        key1 = f[8]
        mo = keys[num1]
        mo.remove(int(key1))
        keys[num1] = mo
        
        mi = keys[num2]
        mi.remove(int(key1))
        keys[num2] = mi
        
    elif len(f) == 7:
        num1 = f[2]
        key1 = f[6]
        mo = keys[num1]
        mo.remove(int(key1))
        keys[num1] = mo
        
    else:
        num1 = f[2]
        key2 = f[4]
        
        for jem in keys:
            if jem != num1:
                mi = keys[jem]
                print(mi)
                mi.remove(int(key2))
                keys[jem] = mi
                
print(keys)