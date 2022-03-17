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
            # 인덱스 범위체크
            if 0 <= nx < 16 and 0 <= ny < 16:
                # 벽이아니고 방문한적없으면
                if miro[nx][ny] != 1 and visited[nx][ny] == 0:
                    # 방문체크
                    visited[nx][ny] = 1
                    # 도착지면
                    if miro[nx][ny] == 3:
                        return 1
                    # 아니면 q에 추가
                    else:
                        Q.append([nx, ny])
    # Q비었는데 도착지 못찾으면 0출력
    else:
        return 0


for _ in range(10):
    tc = input()
    miro = [list(map(int, input()))for _ in range(16)]
    for x in range(16):
        for y in range(16):
            if miro[x][y] == 2:
                start = [x, y]
    visited = [[0]*16 for _ in range(16)]
    Q = []
    print(f'#{tc} {BFS(start[0], start[1])}')