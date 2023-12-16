import math

n, m = list(map(int, input().split(" ")))
s = input()
t = input()

k = 0
# Generate buffers
if n < m:
    dif = len(s) - len(t)
    tNew = t * math.ceil(len(s) / len(t))
    for i in range(n):
        # do the fancy thing
        to_remove = i * dif
        
        # Remove the first to_remove elements
        tNewNew = tNew
        tNewNew = tNewNew[to_remove:]
        
        # Add some new elements
        for j in range(to_remove):
            tNewNew += t[j % len(t)]
            
        # Now, we iterate like normal people
        for m in range(len(s)):
            if s[m] == tNewNew[m]:
                k += 1
elif m > n:
    dif = len(t) - len(s)
    sNew = s * math.ceil(len(t) / len(s))
    for i in range(m):
        # do the fancy thing
        to_remove = i * dif
        
        # Remove the first to_remove elements
        sNewNew = sNew
        sNewNew = sNewNew[to_remove:]
        
        # Add some new elements
        for j in range(to_remove):
            sNewNew += s[j % len(s)]
            
        # Now, we iterate like normal people
        for m in range(len(t)):
            if t[m] == sNewNew[m]:
                k += 1
else:
    # Simple iteration
    for l in range(len(t)):
        if t[l] == s[l]:
           k += n
print(k)
