ques = int(input())
n = int(input())
dmoj = []
peg = []
dmoj = sorted(list(map(int, input().split())))
peg = sorted(list(map(int, input().split())))

out = 0 
if ques == 2:
    # Flip one of the lists
    dmoj.reverse()
    
for j in range(n):
    out += max(dmoj[j], peg[j])
        
print(out)