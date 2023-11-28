n, m = list(map(int, input().split(" ")))
x = input()
ms = list(map(int, input().split(" ")))

c = 0
ma = False

lookup = []
f = 0
for m in range(0, n):
    if x[m] == "0":
        lookup.append([m, ms[f]])
        f += 1
lookup = sorted(lookup, key=lambda maa: maa[1])  
print(lookup)

for fook in lookup:
    asa = x[:fook[1]]
    x = x.removeprefix(asa + "0")
    x += asa
    print(x)
    
print(x)