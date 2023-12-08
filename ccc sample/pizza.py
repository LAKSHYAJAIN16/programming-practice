import math
n, s, o, t = list(map(int, input().split(" ")))
dict = {}
things = 0

for j in range(n):
    slices, type = input().split(" ")
    slices = int(slices)
    if dict.get(type, None) == None:
        dict[type] = slices
        things += 1
    else:
        if (dict[type] // s) != ((dict[type] + slices) // s):
            things += 1
        dict[type] += slices

print(int(math.ceil(things / o)) * t)