
# 나누는 함수
def who(start, end):
    if start == end:
        return start
    # 1대1로 만들어서 승부를 봐서 승자를 찾아내야함
    a = who(start, (start+end)//2)
    b = who((start + end)//2 + 1, end)
    # 1명씩 뽑았으면 승자를 찾아내자
    return who_win(a, b)

# 승자정하는 함수
def who_win(p1, p2):
    # 서로 같은 카드일때
    if what_card[p1] == what_card[p2]:
        return p1
    # p1이 가위로 이긴경우 -2 나머지로이긴경우 1
    elif what_card[p1] - what_card[p2] == 1 or what_card[p1] - what_card[p2] == -2:
        return p1
    # p2가 이겼을 경우
    else:
        return p2


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    what_card = list(map(int, input().split()))
    # 0번인덱스가 사실 1번사람 이니까
    print(f'#{tc} {who(0, N-1)+1}')
