import sys
sys.stdin = open("input.txt", "r")



# 델타이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(n, cx, cy, num):
    if n == 7:
        res.add(num)
        return
    for k in range(4):
        nx = cx + dx[k]
        ny = cy + dy[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            DFS(n+1, nx, ny, num + arr[cx][cy])

T = int(input())

for tc in range(1, T+1):
    arr = [input().split()for _ in range(4)]
    res = set()
    for x in range(4):
        for y in range(4):
            DFS(0, x, y, '')
    print(f'#{tc} {len(res)}')