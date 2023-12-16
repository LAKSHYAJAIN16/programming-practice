n = int(input())
l2 = input().split(" ")
l3 = input().split(" ")

dict = {
    
}

out = "good"
for m in range(n):
    name_1 = l2[m]
    name_2 = l3[m]
    
    if name_2 == name_1:
        out = "bad"
        break
    
    if name_2 in dict:
        if dict[name_2] != name_1:
            out = "bad"
            break
    else:
        if name_1 in dict:
            if dict[name_1] != name_2:
                out = "bad"
                break
            else:
                dict[name_2] = name_1
        else:
            dict[name_2] = name_1 
print(out)