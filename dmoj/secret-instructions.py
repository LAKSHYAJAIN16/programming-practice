dir = ""
outs = []
while True:
    x = input()
    if x == "99999":
        break
    else:
        dirs = int(x[0]) + int(x[1])
        direction = ""
        if dirs == 0:
            direction = dir
        else:
            if dirs % 2 == 0:
                direction = "right"
            else:
                direction = "left"
        dir = direction
    buf = x[2:]
    outs.append([direction, buf])
    
for m in outs:
    print(m[0], m[1])