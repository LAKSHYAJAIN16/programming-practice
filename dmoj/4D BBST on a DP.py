n = int(input())
chars = input()

string = ""
char_map = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8,
    "i" : 9,
    "j" : 10,
    "k" : 11,
    "l" : 12,
    "m" : 13,
    "n" : 14,
    "o" : 15,
    "p" : 16,
    "q" : 17,
    "r" : 18,
    "s" : 19,
    "t" : 20,
    "u" : 21,
    "v" : 22,
    "w" : 23,
    "x" : 24,
    "y" : 25,
    "z" : 26
}

l = char_map[chars[0]]
r = char_map[chars[0]]
string += chars[0]

for k in range(1, len(chars)):
    index = char_map[chars[k]]
    if index <= l:
        l = index
        m = ""
        m += chars[k]
        m += string
        string = m
    else:
        r = index
        m = ""
        m += string
        m += chars[k]
        string = m
print(string)   