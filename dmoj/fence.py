import math

N = int(input())
fences = list(map(int, input().split(" ")))

k = 0
for n in range(math.floor(math.pow(fences, 1/2)), 0, -2):
    
