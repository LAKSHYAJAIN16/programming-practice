# grids = [[],[],[],[],[]]

# for j in range(1, 21):
#     grids[j // 5] = input().split(" ")
        
# grids -> sample
grids = [
    [
        [2, 64, 4, 32],
        [8, 64, 0, 4],
        [4, 4, 4, 0],
        [0, 0 ,0 ,0]
    ]
]

vals = []

def left(grid):
    # Map every line and check if we have similar pieces
    return_grid = grid.copy()
    for n in range(0,4):
        for m in range(0,3):
            if return_grid[n][m] == return_grid[n][m + 1]:
                return_grid[n][m] = grid[n][m] * 2
                return_grid[n][m + 1] = 0
                
    # Now,  make everything go left, keeping in account the zeroes
    ret_ret_grid = return_grid
    for i in range(0, 4):
        for j in range(1, 4):
            if ret_ret_grid[i][j] == 0:
                continue
            
            delta = j
            for k in range(j, -1, -1):
                if ret_ret_grid[i][k] == 0:
                    delta = k
            ret_ret_grid[i][delta] = ret_ret_grid[i][j]
            
            if delta != j:
                ret_ret_grid[i][j] = 0

    return ret_ret_grid.copy()

def right(grid):
    # Map every line and check if we have similar pieces
    return_grid = grid.copy()
    for n in range(0,4):
        for m in range(3, 0, -1):
            if return_grid[n][m] == return_grid[n][m -  1]:
                return_grid[n][m] = grid[n][m] * 2
                return_grid[n][m - 1] = 0

    # Now,  make everything go right, keeping in account the zeroes
    ret_ret_grid = return_grid
    for i in range(0, 4):
        for j in range(2, -1, -1):
            if ret_ret_grid[i][j] == 0:
                continue
            
            delta = j
            for k in range(j, 4):
                if ret_ret_grid[i][k] == 0:
                    delta = k
            ret_ret_grid[i][delta] = ret_ret_grid[i][j]
            
            if delta != j:
                ret_ret_grid[i][j] = 0
                
    return ret_ret_grid.copy()

def top(grid):
    # Map every line and check if we have similar pieces
    return_grid = grid.copy()
    for n in range(0,4):
        for m in range(0,3):
            for k in range(m + 1, 3):
                if return_grid[k][n] == 0:
                    continue
                if return_grid[m][n] == return_grid[k][n]:
                    return_grid[m][n] = grid[m][n] * 2
                    return_grid[k][n] = 0
                if return_grid[m][n] != return_grid[k][n]:
                    break
                    
    # Now,  make everything go up, keeping in account the zeroes
    ret_ret_grid = return_grid.copy()
    for i in range(0, 4):
        for j in range(0, 4):
            if ret_ret_grid[j][i] == 0:
                continue
            
            delta = j
            for k in range(j, -1, -1):
                if ret_ret_grid[k][i] == 0:
                    delta = k
            ret_ret_grid[delta][i] = ret_ret_grid[j][i]
            
            if delta != j:
                ret_ret_grid[j][i] = 0

    return ret_ret_grid.copy()

def bottom(grid):
    # Map every line and check if we have similar pieces
    return_grid = grid.copy()
    for n in range(0,4):
        for m in range(3, 0, -1):
            if return_grid[m][n] == return_grid[m - 1][n]:
                return_grid[m][n] = grid[m][n] * 2
                return_grid[m - 1][n] = 0

    # Now,  make everything go right, keeping in account the zeroes
    ret_ret_grid = return_grid
    for i in range(0, 4):
        for j in range(2, -1, -1):
            if ret_ret_grid[j][i] == 0:
                continue
            
            delta = j
            for k in range(j, 4):
                if ret_ret_grid[k][i] == 0:
                    delta = k
            ret_ret_grid[delta][i] = ret_ret_grid[j][i]
            
            if delta != j:
                ret_ret_grid[j][i] = 0
                
    return ret_ret_grid.copy()

def same_grids(grid1, grid2):
    for i in range(0, len(grid1)):
        for j in range(0, len(grid1[0])):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True

# Play 2048
def game(grid):
    # Grid
    print("\n")
    print("Grid Right now : ")
    for j in grid.copy():
        print(str(j))
    step = input("Choose Step : ")
    if step == "l":
        game(left(grid.copy()))
    elif step == "r":
        game(right(grid.copy()))
    elif step == "t":
        game(top(grid.copy()))
    elif step == "b":
        game(bottom(grid.copy()))
    else:
        print("WTF BRO")
        game(grid.copy())
    
game(grids[0].copy())