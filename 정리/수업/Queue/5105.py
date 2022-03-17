import sys
sys.stdin = open("input.txt", "r")

def BFS(x, y):
    Q.append([x, y])
    while Q:
        now = Q.pop(0)
        # 델타이동 상우하좌
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for k in range(4):
            nx = now[0] + dx[k]
            ny = now[1] + dy[k]
            # 인덱스 범위 내이고
            if 0 <= nx < N and 0 <= ny < N:
                # 통로나 출구고 방문하지 않았으면 거리기록
                if miro[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[now[0]][now[1]] + 1
                    # 도착하면 함수 종료
                    if miro[nx][ny] == 3:
                        return visited[nx][ny]-1
                    # 도착지 아니었으면 q에 추가
                    else:
                        Q.append([nx, ny])
    # 출구 못찾고 끝났으면
    else:
        return 0

T = int(input())
# 0은 통로 1은 벽, 2는 출발 3은 도착
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if miro[x][y] == 2:
                start = [x, y]
    # 큐
    Q = []
    print(f'#{tc} {BFS(start[0], start[1])}')



