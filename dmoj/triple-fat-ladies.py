import math
t = int(input())

for m in range(t):
    num = int(input())
    # calculate
    num = 192 + (250 * math.floor(((num - 192) / 250) + 1))
    print(num)