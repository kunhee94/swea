import sys
sys.stdin = open("input.txt","r")


T = int(input())

for tc in range(1, T + 1):
    # 노드 갯수, 리프노드갯수, 값을출력할 노드번호
    V, M, L = map(int, input().split())
    tree = [0]*(V+1)
    for _ in range(M):
        num, val = map(int, input().split())
        tree[num] = val
        #  잎 노드가 홀수
    if V % 2:
        for i in range(V, 1, -2):
            tree[i//2] = tree[i]+tree[i-1]
        # 짝수
    else:
        for i in range(V - 1, 1, -2):
            tree[V//2] = tree[V]
            tree[i // 2] = tree[i] + tree[i - 1]

    print(f'#{tc} {tree[L]}')


