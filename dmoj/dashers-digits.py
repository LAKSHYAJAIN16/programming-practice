n, m = list(map(int, input().split(" ")))
x = input()
ms = list(map(int, input().split(" ")))

c = 0
ma = False
while ma == False:
    f = x[c]
    if f == "0":
        ms[c] -= 1
        if ms[c] <= 0:
            ms.remove(0)
            if len(ms) == 0:
                x = x.removeprefix("0")
                ma = True
        else:
            x = x.removeprefix("0")
            x += "0"
            if c == m - 1:
                c = 0
            else:
                c += 1
    else:
        x = x.removeprefix(f)
        x += f
        
print(x)