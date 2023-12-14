ni = int(input())
thresh = (ni * (ni-1) / 2) / 2

m = 0

for i in range(1, ni - 1):
    sum = i * (ni - 1) - (i * (i - 1)) / 2
    if sum >= thresh:
        print(i)
        break