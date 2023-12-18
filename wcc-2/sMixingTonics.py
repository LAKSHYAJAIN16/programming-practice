l = int(input())
acid = 250
water = 0

for j in range(l):
    m = input()
    if m == "Acidize":
        acid += 50
    if m == "Dilute":
        water += 100