import sys
sys.stdin = open("input.txt", "r")


def BFS(start, end):
    Q = []
    Q.append(start)
    visited[start] = 1
    while Q:
        now = Q.pop(0)
        for y in range(1, V+1):
            if arr[now][y] and visited[y] == 0:
                visited[y] = visited[now] + 1
                Q.append(y)
                if y == end:
                    return visited[y]
    else:
        return 1
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
        arr[end][start] = 1
    S, G = map(int, input().split())
    # 방문표시
    visited = [0] * (V+1)

    res = BFS(S, G)
    print(f'#{tc} {res-1}')
