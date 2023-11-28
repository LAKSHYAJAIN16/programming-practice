n = int(input())
out = []

EPSILON = 0.1

def cantor(n_b, n_e):
    print("hi!")
    point_beg = (n_e - n_b) / 3
    point_end = point_beg * 2
    
    if abs(point_beg - point_end) <= EPSILON:
        return
    else:
        if point_beg % 1 <= EPSILON:
            out.append(point_beg)
        
        if point_end % 1 <= EPSILON:
            out.append(point_end)
            
        print(point_beg, point_end)

cantor(0, 12)
print(out)