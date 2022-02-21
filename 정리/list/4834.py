def my_max(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    return num[-1]

def my_count(a,k):
    cnt = 0
    for i in a:
        if i == k:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cards =list(map(int,input()))
    result = {} # 카드와 카드장수를 딕셔너리 형식으로 담을것
    # cards를 돌면서 {카드숫자:카드갯수}딕셔너리를 만들어서 result에 저장
    for card in cards:
        result[card]= my_count(cards,card)
    max_card = []   # result의 밸류값 모음

    for i in result:
        max_card.append(result[i])   # 밸류값들을 max_card에 저장
    ks = []                          # 가장 많은 카운트를 가진 키들의 목록
    for i in result:
        if result[i] == my_max(max_card):
            ks.append(i)
    m = my_max(ks)                  # ks 중 에서 가장 큰 값을 가진 키를 찾는다.
    print(f'#{tc} {m} {result[m]}') # 출력