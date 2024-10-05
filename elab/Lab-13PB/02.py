def index_trans(str):
    if str.isnumeric():
        return int(str)
    else:
        if str == 'A':
            return 1
        else:
            return 10

def cal_score(ls):
    sum_s = 0
    i = 0
    while i < len(ls):
        if sum_s > 16:
            break
        sum_s += index_trans(ls[i])
        i += 1       
    return sum_s

#main
bot_total = int(input())
cards = []
for i in range(bot_total):
    draw_card = str(input())
    cards.append(draw_card.split())

result = []
for hands in cards:
    result.append(cal_score(hands))

for score in result:
    if score <= 21:
        print(score)
    else:
        print("busted")