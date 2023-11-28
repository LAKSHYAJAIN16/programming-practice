t = int(input())
out = []
for j in range(1,t + 1):
    n = int(input())
    l = []
    for f in range(1, n + 1):
        mn = int(input())
        l.append(mn)
    l.sort()
    m = l[-1]
    out.append(m)
    
print(out)