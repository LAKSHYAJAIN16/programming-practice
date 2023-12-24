k = int(input())
a_w = 0
b_w = 0

for k in range(0, k):
    a = 0
    b = 0
    for j in range(0, 5):
        stri = input().split(" ")
        if (stri[0] == "R" and stri[1] == "S") or (stri[0] == "P" and stri[1] == "R") or (stri[0] == "S" and stri[1] == "P"):
            a += 1
        if (stri[1] == "R" and stri[0] == "S") or (stri[1] == "P" and stri[0] == "R") or (stri[1] == "S" and stri[0] == "P"):
            b += 1
    if a > b:
        a_w += 1
    elif b > a:
        b_w += 1
        
if a_w > b_w:
    stringy = "A" + " " + str(a_w-b_w)
    print(stringy)
elif b > a:
    stringy = "B" + " " + str(b_w-a_w)
    print(stringy) 
else:
    print("TIE")  