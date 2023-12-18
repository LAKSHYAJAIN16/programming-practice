k, m = list(map(int, input().split(" ")))
phones_raw = []
phones = []

for l in range(k):
    x = input()
    phones_raw.append(x)
    phones.append(x.replace("-","").split())
    
type1 = []
type2 = []
type3 = []
for p in range(m):
    inputThing = input().split(" ")
    if len(inputThing) == 4:
        type1.append(inputThing[3])
    else:
        if inputThing[2] == "a":
            type2.append([inputThing[3],inputThing[6]])
        else:
            type3.append([inputThing[3],inputThing[6]])

def valid(phone, type1, type2, type3):
    for t1 in type1 :
        if t1 in phone[0]:
            return False
    for t2 in type2:
        if phone[0][int(t2[1])] != t2[0]:
            return False
    for t3 in type3:
        if phone[0][int(t3[1])] == t3[0]:
            return False
    return True
    
i = 0          
for phone in phones:
    if valid(phone, type1, type2, type3) == True:
        print(phones_raw[i])
        break
    i += 1