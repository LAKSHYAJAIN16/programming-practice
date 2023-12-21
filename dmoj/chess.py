n , m = list(map(int, input().split(" ")))

things = {
    
}

things_2 = {
    
}

# Get input
for j in range(m):
    inp = [*input()]
    things[str(j)] = []
    for k in range(n):
        char = inp[k]
        if char == "*":
            things[str(j)].append(k)
            if str(k) in things_2:
                things_2[str(k)].append(j)
            else:
                things_2[str(k)] = [j]

out = 0
# Cycle through each key
for key1 in things:
    if len(things[key1]) >= 2:
        out += things[key1][0]
        
for key2 in things_2:
    if len(things_2[key2]) >= 2:
        out += things_2[key2][0]
        
print(out)