import sys
sys.stdin = open("input.txt", "r")


def DFS(sx, sy, s):
    global cnt

    if s == N:
        cnt += 1
        return

    if sx < 0 or sx >= N or sy < 0 or sy >= N:
        return

    # 체스판 전체 범위 팔방에 퀸이 없으면 퀸놓기
    put = 1
    # 상 체크
    for x in range(sx):
        if arr[x][sy]:
            put = 0
            break
    # 왼쪽 체크
    for y in range(sy):
        if arr[sx][y]:
            put = 0
            break

    # 대각선 체크
    # 좌상 체크
    nx = sx - 1
    ny = sy - 1
    while 0 <= nx < N and 0 <= ny < N:
        if arr[nx][ny]:
            put = 0
            break
        nx -= 1
        ny -= 1
    # 우상 체크
    nx = sx - 1
    ny = sy + 1
    while 0 <= nx < N and 0 <= ny < N:
        if arr[nx][ny]:
            put = 0
            break
        nx -= 1
        ny += 1
    # 다체크 했는데 put이 1이면 말을 놓고 DFS

    # 말을 놓을 수 있다면
    if put == 1:
        arr[sx][sy] = 1
        DFS(sx + 1, 0, s + 1)
        # 다 돌아 봤는데 아니었으면 말치우고
        arr[sx][sy] = 0

    # 옆칸 확인하러가기
    DFS(sx, sy + 1, s)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 체스판
    arr = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        DFS(i, 0, 0)

    print(f'#{tc} {cnt}')