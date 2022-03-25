import sys
sys.stdin = open("input.txt", "r")


def DFS(n, cx, cy, v, cnt):
    global sx, sy, res
    # 종료조건
    if n > 3:
        return
    # 정답 갱신
    if n == 3 and cx == sx and cy == sy and res < cnt:
        res = cnt
        return

    for k in range(n, n+2):
        nx, ny = cx+dx[k], cy+dy[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] not in v:
            DFS(k, nx, ny, v+[arr[nx][ny]], cnt+1)



dx = [1, 1, -1, -1, 0]
dy = [-1, 1, 1, - 1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = -1
    for sx in range(N-2):
        for sy in range(1, N-1):
            DFS(0, sx, sy, [], 0)
    print(f'#{tc} {res}')