k, d = list(map(int, input().split()))
digits = list(map(int, input().split()))

# Sort the digits
digits.sort()

num = -1

# Check if d is even or odd
if len(digits) == 1:
    if digits[0] == 0:
        num = -1
    else:
        num = digits[0]
else:
    if digits[0] == 0:
        if k % 2 == 0:
            num = int(str(digits[1]) * k)
        else:
            num = int(str(digits[1]) * (k // 2) + "0" + str(digits[1]) * (k // 2))
    else:
        num = int(str(digits[0]) * k)

    if num == 0:
        num = -1

print(num)