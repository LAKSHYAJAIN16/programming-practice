j = int(input())
a = int(input())
g = 0
shirts = {}

for m in range(j):
    size = input()
    shirts[m + 1] = size
    
for f in range(a):
    size, num = input().split(" ")
    num = int(num)
    if num in shirts:
        if (shirts[num] == "L" and size == "M") or (shirts[num] == "L" and size == "S") or (shirts[num] == "M" and size == "S") or (shirts[num] == size):
            g += 1
            del shirts[num]
            
print(g)