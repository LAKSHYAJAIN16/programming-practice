import sys
T = input()
S = input()

pairs = [
    
]

k = 0

# Calculate all pairs for the data
if len(S) % 2 == 0:
    for j in range(0,len(S), 2):
        pairs.append([S[j] + S[j+1]])
    if len(S) != 2:
        pairs.append([S[0] + S[len(S)-1]])
else:
    for j in range(len(S) - 1):
        pairs.append()
        
print(pairs)