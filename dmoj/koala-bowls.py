sum = 0
def fn(m):
    global sum
    sum += int(m)
    
n = int(input())
ks = list(map(fn, input().split()))
avg = sum / n
if avg % 1 == 0:
    print(n)
else:
    print(int(1 // (avg % 1)))