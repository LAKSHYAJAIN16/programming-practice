x = int(input())
dict = {}
for i in range(x):
    s = input().split(" ")
    if s[0] in dict:
        dict[s[0]].append([0,s[1]])
    else:
        dict[s[0]] = [[0,s[1]]]
        
    if s[1] in dict:
        dict[s[1]].append([0,s[0]])
    else:
        dict[s[1]] = [[0,s[0]]]
    
y = int(input())
for j in range(y):
    s = input().split(" ")
    if s[0] in dict:
        dict[s[0]].append([1,s[1]])
    else:
        dict[s[0]] = [[1,s[1]]]
    
    if s[1] in dict:
        dict[s[1]].append([1,s[0]])
    else:
        dict[s[1]] = [[1,s[0]]]
    
g = int(input())
viols = 0
for k in range(g):
    group = input().split(" ")
    for m in group:
        if m in dict:
            buf = dict[m]
            for l in buf:
                if l[0] == 0:
                    if not(l[1] in group):
                        viols += 1
                if l[0] == 1:
                    if l[1] in group:
                        viols += 1
        else:
            continue
print(viols // 2)
        