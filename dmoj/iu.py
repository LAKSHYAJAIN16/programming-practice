n = int(input())
string = [*input()]
s = 0
for k in range(len(string)):
    if k % 2 == 0:
        if string[k] != "I":
            s += 1
    if k % 2 == 1:
        if string[k] != "U":
            s += 1
            
print(s // 2)