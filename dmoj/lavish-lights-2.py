n , k = list(map(int, input().split(" ")))
i = list(map(int, input().split(" ")))
t = []

for _ in range(k):
    t.append(int(input()))

founds = dict(map(lambda item: (item, -1), t))
for l in range(0, n):
    f = False
    for m in t:
        if m % i[l] != 0:
            founds[m] = l + 1
            t.remove(m)
            
for j in founds:
    print(founds[j])
            