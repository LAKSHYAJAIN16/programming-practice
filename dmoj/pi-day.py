n = int(input())
k = int(input())

sols = 0

def compute(stage, n_s, j):
    # Check if we've gone too far
    if stage == k - 1:
        global sols
        sols += 1
    else: 
        div = n_s // (k - stage)
        for l in range(j, div + 1):
            compute(stage + 1, n_s - l, l)

compute(0, n, 1)
print(sols)