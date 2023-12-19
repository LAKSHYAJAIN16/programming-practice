t,n = list(map(int, input().split(" ")))
chars = [*"abcdefghijklmnopqrstuvwxyz"]

outs = []
for k in range(t):
    out = ""
    inp = input()
    for l in inp:
        if l != " ":
            index = chars.index(l)
            out += chars[index - n]    
        else:
            out += " "
    outs.append(out)
    
for out in outs:
    print(out)