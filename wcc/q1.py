a, b = list(map(int, input().split(" ")))
cards_1 = input().split(" ")
cards_1_set = {}
cards_2 = input().split(" ")
cards_2_set = {}

pairs1 = 0
pairs2 = 0
for card in cards_1:
    if card in cards_1_set:
        cards_1_set[card] += 1
        if cards_1_set[card] % 2 == 0:
            pairs1 += 1
    else:
        cards_1_set[card] = 1
    
for card_2 in cards_2:
    if card_2 in cards_2_set:
        cards_2_set[card_2] += 1
        if cards_2_set[card_2] % 2 == 0:
            pairs2 += 1
    else:
        cards_2_set[card_2] = 1
        

if pairs2 > pairs1:
    print("Bob wins with",pairs2,"pairs")
else:
    print("Alice wins with",pairs1,"pairs")