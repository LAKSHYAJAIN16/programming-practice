n = int(input())
k = list(map(int, input().split(" ")))
k.sort()

# Split k into two parts
out = []
if n % 2 != 0:
    out.append(str(k[n // 2]))
    del k[n // 2]
    chunk1 = k[0:n // 2]
    chunk1.reverse()
    chunk2 = k[n // 2:]
    for j in range(n // 2):
        out.append(str(chunk2[j]))
        out.append(str(chunk1[j]))
else:
    chunk1 = k[0:n // 2]
    chunk1.reverse()
    chunk2 = k[n // 2:]
    for j in range(n // 2):
        out.append(str(chunk1[j]))
        out.append(str(chunk2[j]))
    
print(" ".join(out))
