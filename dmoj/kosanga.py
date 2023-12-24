n = int(input())
stri = list(map(int, [*input()]))

g = 0
for m in range(len(stri)):
    if stri[m] == 0:
        # Go look at both sides
        u1 = len(stri) - m - 1
        u2 = m
        u = max(u1, u2)
        f = 0
        for i in range(u):
            t1 = m - i
            t2 = m + i
            if t1 >= 0:
                if stri[t1] == 1:
                    f = i + 1
                    break
            if t2 <= len(stri) - 1:
                if stri[t2] == 1:
                    f = i + 1
                    break
        g += f
        
print(g)