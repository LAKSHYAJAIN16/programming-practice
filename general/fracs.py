num = int(input())
denom = int(input())

if num == 0:
    print(0)
else:
    whole = num // denom
    num1 = num % denom
    
    # Check if coprime
    nums = []
    for i in range(2, (num1) // 2):
        if num1 % i == 0 and denom % i == 0:
            nums.append(i)
            
    mul = 1
    for m in nums:
        mul *= m
    frac1 = num1 // mul
    frac2 = denom // mul 
    print(whole, 
    