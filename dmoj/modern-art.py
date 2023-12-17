M = int(input())
N = int(input())
K = int(input())
grid = {}

f = 0
for i in range(1, K+1):
    q, n = input().split(" ")
    n = int(n)
    if q == "R":
        for j in range(1,N+1):      
            if str(n)+":"+str(j) in grid:
                grid[n*10+j] += 1
                if grid[str(n)+":"+str(j)] % 2 == 1:
                    f += 1
                else:
                    f -= 1
            else:
                grid[str(n)+":"+str(j)] = 1
                f += 1
                
    elif q == "C":
        for m in range(1, M+1):
            if str(m)+":"+str(n) in grid:
                grid[str(m)+":"+str(n)] += 1
                if grid[str(m)+":"+str(n)] % 2 == 1:
                    f += 1
                else:
                    f -= 1
            else:
                grid[str(m)+":"+str(n)] = 1
                f += 1
print(f)