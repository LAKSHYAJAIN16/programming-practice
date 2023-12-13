s = input()

buf = ""
num = ""
sign = ""
mode = 0

for k in s:
    if mode == 0:
        if k != "-" and k != "+":
            buf += k
        else:
            if k == "+":
                sign = "tighten"
            else:
                sign = "loosen"
            mode = 1
            
    if mode == 1 and (k != "+" and k!= "-"):
        if k != "1" and k != "2" and k!= "3" and k != "4" and k != "5" and k != "6" and k!= "7" and k!= "8" and k != "9" and k !="0":
            print(buf,sign,num)
            buf = k
            num = ""
            mode = 0
        else:
            num += k
            
            
print(buf,sign,num)
            