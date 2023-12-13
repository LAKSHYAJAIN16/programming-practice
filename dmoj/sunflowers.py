N = int(input())
matrix = []

def check_mat(m):
    for i in m:
        if sorted(i) == i:
            continue
        else:
            return False
    return True
 
def print_mat(m):
    print("".join(list(map(str, m))))    
         
for i in range(N):
    matrix.append(list(map(int, input().split(" "))))
    
# Check matrix
if check_mat(matrix) == True:
    print_mat(matrix)
else:
    # First Thing
    mat_2 = matrix
    for m in range(N):
        for k in range(N):
            m[k][m]