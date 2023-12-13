s1 = input().lower()
s2 = input().lower()
s3 = input().lower()

MAP_2 = {
    "a" : ".",
    "b" : ".",
    "c" : ".",
    "d" : ".",
    "e" : ".",
    "f" : ".",
    "g" : ".",
    "h" : ".",
    "i" : ".",
    "j" : ".",
    "k" : ".",
    "l" : ".",
    "m" : ".",
    "n" : ".",
    "o" : ".",
    "p" : ".",
    "q" : ".",
    "r" : ".",
    "s" : ".",
    "t" : ".",
    "u" : ".",
    "v" : ".",
    "w" : ".",
    "x" : ".",
    "y" : ".",
    "z" : ".",
    " " : "."
}

for i in range(len(s1)):
    I = s1[i]
    J = s2[i]
    MAP_2[J] = I

out = ""
for k in s3:
    out += MAP_2[k]
    
print(out.upper())