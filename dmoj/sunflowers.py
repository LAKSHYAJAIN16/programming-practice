N = int(input())
matrix = []

def check_mat(m):
    r = True
    for i in m:
        if sorted(i) != i:
            r = False
            break
    return r
    
 
def print_mat(m):
    for k in m:
        print(" ".join(list(map(str, k))))
         
for i in range(N):
    matrix.append(list(map(int, input().split(" "))))
    
# Check matrix
if check_mat(matrix) == True:
    print_mat(matrix)
else:
    # First Thing
    matrix_2 = []
    for m in range(N - 1, -1):
        matrix_2.append(reversed(matrix[m]))
    # print(matrix_2)    
    if check_mat(matrix_2) == True:
        print_mat(matrix_2)
    else:
        # Second Thing
        matrix_3 = []
        for k in range(N - 1, -1):
            new_thing = []
            for l in range(N):
                new_thing.append(matrix[l][k])
            matrix_3.append(new_thing)
        # print(matrix_3)
        if check_mat(matrix_3) == True:
            print_mat(matrix_3)   
        else:
            # Third Thing
            matrix_4 = []
            # print(matrix_4)
            for m in range(N - 1, -1):
                matrix_4.append(reversed(matrix_3[m]))
            print(matrix_4)