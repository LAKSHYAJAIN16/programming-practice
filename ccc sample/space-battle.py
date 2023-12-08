import math
t, h, d, r = list(map(int, input().split(" ")))
l = []

for i in range(t):
    eh, ed, er = list(map(int, input().split(" ")))
    time_taken = (math.ceil((eh - d) / d)) * r
    our_health = h
    our_health -= (round(time_taken / er)) * ed
    our_health -= ed
    if our_health >= 0:
        l.append(h - our_health)
        
        
l.sort()
k = 0
sum = 0
for i in l:
    if (sum + i) <= h:
        sum += i
        k += 1
    else:
        break
    
print(k)