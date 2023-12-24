m = int(input())
ts = list(map(int, input().split(" ")))
ks = list(map(int, input().split(" ")))

ar = 0
for i in range(m):
    ar += ((ts[i] + ts[i + 1]) / 2) * ks[i]
    
print(ar)