n = int(input())
line1 = input().split(" ")
line2 = input().split(" ")
oopsies = 0
f = 0

# Check Line 1
for m in range(0, n):
    if line1[m] == "1":
        if n - 1 == m:
            f += 3
        else:
            if line1[m + 1] == "1":
                oopsies += 2
            if line2[m] == "1":
                oopsies += 2
            f += 3

# Check Line 2
for l in range(0, n):
    if line2[l] == "1":
        if n - 1 == l:
            f += 3
        else:
            if line2[l + 1] == "1":
                oopsies += 2
            f += 3

sides = f - oopsies
print(sides)