import math

l1, b1 = list(map(int, input().split(" ")))
l2, b2 = list(map(int, input().split(" ")))
l3, b3 = list(map(int, input().split(" ")))

# Basic Solution
ar = l1*b1 + l2*b2 + l3*b3
if math.sqrt(ar).is_integer() == True:
    if l1 != l2 and l1 != l3 and l2 + l3 == l1 and b2 == b3:
        print("YES")
    elif l2 != l1 and l2 != l3 and l1 + l3 == l2 and b1 == b3:
        print("YES")
    elif l3 != l1 and l3 != l2 and l1 + l2 == l3 and b2 == b1:
        print("YES")
    elif b1 != b2 and b1 != b3 and b2 + b3 == b1 and l2 == l3:
        print("YES")
    elif b2 != b1 and b2 != b3 and b1 + b3 == b2 and l1 == l3:
        print("YES")
    elif b3 != b1 and b3 != b2 and b1 + b2 == b3 and l2 == l1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")