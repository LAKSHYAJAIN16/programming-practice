n = int(input())
alpaccas = []

for j in range(n):
    input_ = list(map(int, input().split(" ")))
    alpaccas.append([input_[0] + input_[1], input_[0] - input_[1]])
    
print(alpaccas)
    
