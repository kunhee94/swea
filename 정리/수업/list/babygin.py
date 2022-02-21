T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input())) # 카드 받아오기
    cnt_card = [0]*10    # 카드 갯수 세기
    for i in range(len(cards)):
        cnt_card[cards[i]] += 1
    triple = 0
    run = 0
    # print(cnt_card)
    # run 찾기
    i = 0
    while i <= 7:
        if cnt_card[i] and cnt_card[i+1] and cnt_card[i+2]:
            cnt_card[i] -= 1
            cnt_card[i+1] -= 1
            cnt_card[i+2] -= 1
            run += 1
            continue
        i += 1
    j = 0
    while j <= 9:
        if cnt_card[j] >= 3:
            cnt_card[j] -= 3
            triple += 1
            continue
        j += 1
    if (run ==  2 or triple == 2) or (run and triple):
        print(1)
    else:
        print(0)