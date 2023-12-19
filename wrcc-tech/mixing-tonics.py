n = int(input())
acid = 250
water = 0
tank = 0
for m in range(n):
    k = input()
    if k == "Acidize":
        acid += 50
    elif k == "Extract":
        tank += acid * 0.1
        acid *= 0.9
        water *= 0.9
    elif k == "Dilute":
        water += 100
    elif k == "Neutralize":
        vol = acid + water
        acid *= 0.5
        water *= 0.5
        water += vol/2
        
    if acid + water > 500:
        water_to_acid = water / acid + 1
        x = 500 / water_to_acid
        acid = x
        water = (water_to_acid - 1) * x

print(round(tank))