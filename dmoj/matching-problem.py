n, m = list(map(int, input().split(" ")))
s = input()
t = input()
A = s * n
B = t * m
k = 0
for i in range(len(A)):
    if A[i] == B[i]:
        k += 1
        
print(k)