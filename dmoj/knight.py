x1, y1 = list(map(int, input().split(" ")))
x2, y2 = list(map(int, input().split(" ")))

# deltas
xDelta = x2 - x1
yDelta = y2 - y1

# localDels
globdepth = 0
def check_squares(depth, x, y, xTarget, yTarget):
    global globdepth
    if (x + 2 == xTarget and y + 1 == yTarget) or (x - 2 == xTarget and y - 1 == yTarget) or (x - 2 == xTarget and y + 1 == yTarget) or (x + 2 == xTarget and y - 1 == yTarget) or (x + 1 == xTarget and y + 2 == yTarget) or (x - 1 == xTarget and y - 2 == yTarget) or (x - 1 == xTarget and y + 2 == yTarget) or (x + 1 == xTarget and y - 2 == yTarget):
        if depth + 1 < globdepth:
            globdepth = depth + 1
    else:
        # Start targets
        if x <= 6 and y <= 7:
            check_squares(depth + 1, x + 2, y + 1, xTarget, yTarget)
        if x <= 6 and y >= 2:      
            check_squares(depth + 1, x + 2, y - 1, xTarget, yTarget)
        if x >= 3 and y <= 7:
            check_squares(depth + 1, x - 2, y + 1, xTarget, yTarget)
        if x >= 3 and y >= 2:
            check_squares(depth + 1, x - 2, y - 1, xTarget, yTarget)
        if x >= 2 and y <= 6:
            check_squares(depth + 1, x - 1, y + 2, xTarget, yTarget)
        if x >= 2 and y >= 3:
            check_squares(depth + 1, x - 1, y - 2, xTarget, yTarget)
        if x <= 7 and y >= 6:
            check_squares(depth + 1, x + 1, y + 2, xTarget, yTarget)
        if x <= 7 and y >= 3:
            check_squares(depth + 1, x + 1, y - 2, xTarget, yTarget)

check_squares(1, x1, y1, x2, y2)
print(globdepth)