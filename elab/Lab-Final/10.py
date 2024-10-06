def find_strongest_card(ls):
    tmp = ''
    for i in range(len(ls)):
        if i == 0:
            tmp = ls[i]
            continue
        else:
            if index.get(tmp) < index.get(ls[i]):
                tmp = ls[i]
            elif index.get(tmp) == 10 and index.get(tmp) == index.get(ls[i]):
                if big4.get(tmp) < big4.get(ls[i]):
                    tmp = ls[i]
    return tmp

def score(ls):
    tmp = ls
    s = 0
    for i in range(len(tmp)):
        if s < 17: 
            s += index.get(tmp[i])
        else:
            tmp = tmp[:i]
            break
    return s, tmp

index = {
    "A" : 1, 
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}

big4 = {
    "10" : 1,
    "J" : 2,
    "Q" : 3,
    "K" : 4
}

draw = str(input())
hand = draw.split()

total_score = score(hand)[0]
final_hand = score(hand)[1]

print(find_strongest_card(final_hand))
if total_score <= 21:
    print(total_score)
else:
    print("busted")