import math
n, d, k, x = list(map(int, input().split(" ")))

alpaccas = []
for m in range(n):
    alpaccas.append(int(input()))

p = int(input())

DEPRECIATING = (100 - x) / 100

for f in alpaccas:
    if f >= p:
        m = round((math.log10(p) - math.log10(f)) / math.log10(DEPRECIATING))
        k -= m
        
if k >= 0:
    print("YES")
else:
    print("NO")       