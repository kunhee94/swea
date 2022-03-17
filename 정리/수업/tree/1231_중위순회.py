import sys
sys.stdin = open("input.txt", "r")


def in_order(n):
    global result
    if n:
        in_order(ch1[n])
        result += word[n]
        in_order(ch2[n])

for tc in range(1, 11):
    # 정점의 갯수
    V = int(input())
    # 간선의 갯수
    E = V - 1
    word = [0] * (V + 1)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(1, V+1):
        a = list(input().split())
        word[i] = a[1]
        if len(a) == 4:
            ch1[i] = int(a[2])
            ch2[i] = int(a[3])
        elif len(a) == 3:
            ch1[i] = int(a[2])
    result = ''
    in_order(1)
    print(f'#{tc} {result}')