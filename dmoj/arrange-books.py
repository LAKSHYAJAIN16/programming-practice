import math

st = input()
ls=""
ms=""
ss=""
for char in st:
    if char == "L":
        ls += "L"
    elif char == "M":
        ms += "M"
    else:
        ss += "S"
        
finale=ls+ms+ss
co = 0

for i in range(len(st)):
    if st[i] != finale[i]:
        co += 1
        
print(co // 2)