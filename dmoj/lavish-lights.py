n , k = list(map(int, input().split(" ")))
i = list(map(int, input().split(" ")))
t = []

for _ in range(k):
    t.append(int(input()))

out=[]
for l in range(0, k):
    f = False
    for m in range(0, n):
        if t[l] % i[m] != 0:
            out.append(m + 1)
            f  = True
            break
    if f == False:      
        out.append(-1)

for f in out:
    print(f)