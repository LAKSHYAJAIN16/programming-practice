t = int(input())
l = []
    
def evaluate_expression(inp):
    # Check for Parenthesis
    current = ""
    data = []
    state = 0
    
    for k in range(len(inp)):
        if inp[k] == "(" and state != 2:
            state = 2
        elif inp[k] == ")" and state == 2:
            state = 0
        elif inp[k] == "<" or inp[k] == ">" or inp[k] == "~":
            if state == 0:
                data.append([current, inp[k]])
                current = ""
            if state == 2:
                current += inp[k]    
        else:
            current += inp[k]
            
    data[len(data) - 1].append(current)
    print(data)
            
for j in range(t):
    inp = input()
    evaluate_expression(inp)
        
print(l)