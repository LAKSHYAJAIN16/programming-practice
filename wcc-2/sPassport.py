def k():
    id = input().split(": ")[1]
    by = int(input().split(": ")[1])
    iy = int(input().split(": ")[1])
    ey = int(input().split(": ")[1])
    ht = input().split(": ")[1]
    ht_1 = 0
    
    if "cm" in ht:
        ht_1 = int(ht.replace("cm",""))
        if ht_1 > 250:
            return "NO"
    if "ft" in ht:
        ht_1 = int(ht.split("ft")[0])
        ht_2 = int(ht.split("ft")[1].split("in")[0].replace("ft","").replace(str(ht_1),""))
        print(ht_1,ht_2)
        if ht_1 > 8 and ht_2 > 0:
            return "NO"
    cd = int(input().split(": ")[1])
    cl = input().split(": ")[1]
    bw = int(input().split(": ")[1].replace("kg",""))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    cl_to_money = {
        "first" : 1000,
        "business" : 500,
        "economy" : 250
    }
    
    # First thing
    for m in id:
        if m in chars == False:
            return "NO"
        
    # Second thing
    if by > iy:
        return "NO"
    
    # Third thing
    if iy >= ey or iy > 2023:
        return "NO" 
    
    # Fourth thing
    if ey < 2023 or ey - iy > 15:
        return "NO"
    
    money = cl_to_money[cl] + bw * 10 - cd
    return money

n = int(input())
outs = []
for l in range(n):
    outs.append(k())
    
for o in outs:
    print(o)