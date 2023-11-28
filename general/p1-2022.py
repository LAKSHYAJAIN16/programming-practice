n = int(input())
ns = []
for mo in range(0, n):
    ns.append(input().split(" "))

m = int(input())
ms = []
for no in range(0, m):
    ms.append(input().split(" "))

k = int(input())
ks = []
for ko in range(0, k):
    ks.append(input().split(" "))
    
hits = 0
for group in ks:
    for m_1 in ms:
        if ((m_1[0] in group and m_1[1] in group) == True and (m_1[0] in group or m_1[1] in group)) == True:
            hits += 1
            
    for n_1 in ns:
        if ((n_1[0] in group and n_1[1] in group) == False and (m_1[0] in group or m_1[1] in group)) == True:
            hits += 1
            
print(hits // 2)