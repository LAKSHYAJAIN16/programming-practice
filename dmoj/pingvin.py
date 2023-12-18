n = int(input())
x1, y1, z1 = list(map(int, input().split(" ")))
x2, y2, z2 = list(map(int, input().split(" ")))
space = []

for j in range(n):
    space.append([])
    for m in range(n):
        sInput = list(map(int, input()))
        space[j].append([])
        print(space)
        for k in range(n):
            space[j][m] = sInput[k]
        
print(space)