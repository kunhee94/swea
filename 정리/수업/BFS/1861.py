import sys
sys.stdin = open("input.txt", "r")


def BFS(sx, sy):
    Q = []
    Q.append([sx, sy])
    visited[sx][sy] = 1
    s = [arr[sx][sy]]
    # 델타이동 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Q:
        [cx, cy] = Q.pop(0)
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            # 인덱스 범위 안이고 방문 안했고 차이가 1이라면
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and \
                    abs(arr[cx][cy]-arr[nx][ny]) == 1:
                # Q에 넣고
                    Q.append([nx, ny])
                # 방문체크
                    visited[nx][ny] = 1
                # s에 넣어주기
                    s.append(arr[nx][ny])
    return min(s), len(s)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 방문 갯수
    cnt = 0
    # 출발 지점
    num = N*N
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                a, b = BFS(x, y)
                if b > cnt or b == cnt and a < num:
                    cnt = b
                    num = a
    # 제일 긴 방이면서 겹치면 가장 작은 숫자 출력
    print(f'#{tc} {num} {cnt}')
