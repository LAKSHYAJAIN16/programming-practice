import math

d = int(input())
hours = d // 60
delta = d % 60
t = 0

MAPPER = {
    0 : [34],
    1 : [11, 23, 35, 47, 59],
    2 : [10, 22, 34, 46, 58],
    3 : [21, 33, 45, 57],
    4 : [20, 32, 44, 56],
    5 : [31, 42, 55],
    6 : [30, 42, 54],
    7 : [41, 53],
    8 : [40, 52],
    9 : [51],
    10 : [],
    11 : [11],
}

if d >= 60:
    for k in range(0,11):
        N = math.floor(((hours - k + 1) / 12)+1)
        print(N)
        if N > 0:
            t += len(MAPPER[k]) * N
    
# The extra $#!7
map_thing = hours % 12
ar_thing = MAPPER[map_thing]

for m in ar_thing:
    if delta >= m:
        t += 1
    else:
        break
    
print(t)