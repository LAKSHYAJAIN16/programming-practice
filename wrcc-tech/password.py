n = int(input())
c = 0
for k in range(n):
    inp = [*input()]
    if len(inp) != 10:
        continue
    
    # Store the last character
    last = int(inp[-1])
    del inp[-1]
    
    f_3 = 0
    f_2 = 0
    for k in range(0, len(inp) - 2):
        char1 = inp[k]
        char2 = inp[k + 1]
        char3 = inp[k + 2]
        if char1 == char2 and char2 == char3:
            f_3 += 1
        else:
            if char1 == char2:
                f_2 += 1
            elif char2 == char3:
                f_2 += 1
    print(f_3, f_2)             
    if f_3 == 1 and f_2 == 1:
        c += last
print(c)