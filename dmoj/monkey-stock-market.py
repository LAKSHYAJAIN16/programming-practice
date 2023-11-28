n = int(input())
k = list(map(int, input().split(" ")))
s = ""

sum = 0
for f in k:
    sum += f
    
avg = sum / n
fo1 = 1
fo2 = 0
ret_k = sorted(k.copy())

for g in range(0, n):
    if g == n//2 and n % 2 != 0:
        continue
    else:
        print(ret_k)
        if k[g] >= avg:
            ret_k[fo1] = k[g]
            fo1 += 2 
        else:
            ret_k[fo2] = k[g]
            fo2 += 2
            
print(ret_k)