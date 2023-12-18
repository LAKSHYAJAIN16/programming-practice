n = int(input())
vals = [int(item) for item in input().split(" ")]

outs = []
sum_1 = 0
for m in range(0, (n) // 2):
    sum_1 += abs(vals[m] - vals[-(m + 1)])
outs.append(sum_1)
            
for i in range(1, n + 1):
    maxes = []
    for j in range(0, i + 1):
        # Run Two Patterns for each time
        index_1 = j
        index_2 = i - j
        
        # trim array
        ar = vals.copy()
        if index_1 != 0:
            del ar[:index_1]
        if index_2 != 0:
            del ar[-index_2:]
        
        if ar == []:
            # continue
            continue
        else:
            # do the weird calculation
            sum = 0
            for m in range(0, (n - i) // 2):
                sum += abs(ar[m] - ar[-(m + 1)])
            maxes.append(sum)
            
    maxes.sort()
    if len(maxes) == 0:
        outs.append(0)
    else:
        outs.append(maxes[0])
    
outs.reverse()
print(" ".join([str(it) for it in outs[1:]]))