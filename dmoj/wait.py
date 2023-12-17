n = int(input())
hash = {}
i = 0
out = []

for j in range(n):
    act1, act2 = input().split(" ")
    act2 = int(act2)
    
    if act1 == "R":
        hash[act2] = i
        i += 1
    if act1 == "W":
        i += act2
    if act1 == "S":
        hash[act2] += 
        i += 1

print(out)