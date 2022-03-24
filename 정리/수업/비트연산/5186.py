import sys
sys.stdin =open('input.txt', 'r')

def find(i, s, li):
    global res
    if res:
        return
    if s == 0:
        res = li[:]
        return
    elif s < 0:
        return
    elif i == 12:
        if s != 0:
            return
    else:
        li[i] = 1
        find(i+1, s-lis[i], li)
        li[i] = 0
        find(i+1, s, li)

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    # 조합 써볼까?
    lis = [2**(-i) for i in range(1, 13)]
    bit = [0] * 12
    res = []
    find(0, N, bit)
    print(res)
    # res 뒤부터 와서 값이 존재하는 부분이 있으면 거기부터 왼쪽만 남기고 다버림
    result = ''
    for i in res:
        result += str(i)
    if result:
        print(f'#{tc} {result.rstrip("0")}')
    else:
        print(f'#{tc} overflow')



