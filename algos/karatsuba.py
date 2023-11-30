import math

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:  
        # Split
        base1 = len(str(x))
        base2 = len(str(y))
        base = 10 ** (math.ceil(max(base1, base2) / 2))

        # Get x1, x0, y1, y0
        x1 = x // base
        x0 = x % base
        y1 = y // base
        y0 = y % base

        z2 = karatsuba(x1, y1)
        z0 = karatsuba(x0, y0)
        z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0
    
        return z2 * base ** 2 + z1 * base + z0
    
print(karatsuba(1210,200))