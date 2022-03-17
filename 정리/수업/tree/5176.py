import sys
sys.stdin = open("input.txt","r")

T = int(input())

def in_order(i):
    global cnt
    # 중위순회로 돌면서 숫자넣으면 되는거였음
    if i <= N:
        in_order(2*i)
        tree[i] = cnt
        cnt += 1
        in_order(2*i+1)

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')