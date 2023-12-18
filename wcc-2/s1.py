chars = "abcdefghijklmnopqrstuvwxyz"
ts = list(map(int, input().split(" ")))
outs = []
for m in range(len(ts)):
    caes = ts[m]
    text = input()
    out = ""
    for n in text:
        ind2 = chars.index(n) - caes
        out += chars[ind2]
    outs.append(out)
    
for k in outs:
    print(k)