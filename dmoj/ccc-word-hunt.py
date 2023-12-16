w = input()
r = int(input())
c = int(input())

grid = []
for i in range(r):
    grid.append(input().split(" "))  
    
# Define buffer
buffer = [[]]

# Loop through grid
for j in range(r):
    for k in range(c):
        if grid[j][k] == w[0]:
            # Add certain vectors to our list
            if k != r-1:
                buffer.append([j,k + 1, w[1]])
            if j != r -1 and k!=r-1:
                buffer.append([j + 1, k + 1, w[1]])
            if j != r - 1:
                buffer.append([j + 1, k, w[1]])
            if j != r-1 and k != 0:
                buffer.append([j])
                