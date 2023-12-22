n, l, s = list(map(int, input().split(" ")))

dict = {
    
}
hits = 0
for k in range(n):
    ai, bi, si = list(map(int, input().split(" ")))
    for ki in range(ai, bi + 1):
        if ki in dict:
            dict[ki] += si
            if dict[ki] >= s:
               hits += 1 
        else:
            dict[ki] = si
            
print(l - hits)