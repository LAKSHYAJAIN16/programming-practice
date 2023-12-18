n = int(input())
check = 0
for j in range(n):
    string = input()
    set1 = []
    set2 = []
    string_2 = string[:-1]
    for k in range(len(string_2) - 2):
        char1 = string[k]
        char2 = string[k + 1]
        char3 = string[k + 2]
        if char1 == char2 and char2 == char3:
            set1.append(char1)
        if char1 == char2:
            set2.append(char1)
        if char2 == char3:
            set2.append(char2)
            
    # remove dp
    set2 = list(dict.fromkeys(set2))
    set1 = list(dict.fromkeys(set1))
    set3 = []
    for j in range(len(set2)):
        if (set2[j] in set1) == False:
            set3.append(set2[j])
            
    if len(set1) == 1 and len(set3) == 1:    
        print("HI!")
        check += int(string[-1])
        
print(check)