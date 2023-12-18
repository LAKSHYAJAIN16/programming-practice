s = input()

# define function to check if it is a palindrome
def is_palin(stra):
    x = len(stra)
    for i in range(x // 2):
        if stra[i] != stra[x - i - 1]:
            return False
    return True

# Calculate all substrings, because why not?
max = 0
for j in range(len(s)):
    # Del first character
    brooklyn = s
    if j != 0:
        brooklyn = s[j:]
    
    # Get all substrings
    for k in range(0, len(brooklyn)):
        sub_str = brooklyn[:k +1]
        if is_palin(sub_str) and len(sub_str) > max:
            max = len(sub_str)
            
print(max)