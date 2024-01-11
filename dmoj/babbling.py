N = int(input())
ls = []

for j in range(N):
    ls.append(int(input()))
    
while True:
    # Control input
    control = int(input())
    
    if control == 77:
        break
    elif control == 88:
        # Merge
        k = int(input())
        
        # Delete the Item
        val = ls[k - 1]
        ls[k] += val
        del ls[k-1]
    elif control == 99:
        # Split
        k = int(input())
        m = int(input())
        i = int((m / 100) * ls[k-1])
        ls.insert(k - 1, i)
        ls[k] = ls[k] - i
    
print(" ".join(list(map(str,ls))))