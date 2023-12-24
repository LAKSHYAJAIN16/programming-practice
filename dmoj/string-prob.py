string = [*input()]
hash_map = {}

for char in string:
    if char in hash_map:
        hash_map[char] += 1
    else:
        hash_map[char] = 1
   
hash_map_2 = dict(sorted(hash_map.items(), key=lambda item: item[1]))
f = 0
if len(hash_map_2) <= 2:
    print(0)
else:
    for k in range(2, len(list(hash_map_2.keys()))):
        keys = list(hash_map_2.keys())
        keys.reverse()
        f += hash_map_2[keys[k]]
    print(f)