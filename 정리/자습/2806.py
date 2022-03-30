import sys
sys.stdin = open("input.txt", "r")


# 체스놓을 수 있는 경우의 수
dx = [1, 1, 1]
dy = [-1, 0, 1]



def DFS(sx, sy, s):
    if s == N:
        return
    for k in range(3):
        nx = sx +dx[k]
        ny = sy +dy[k]
        # arr[nx][ny]기준 체스판 전체 팔방으로 퀸이 없으면 놓을 수 있음
        for i in range(N):
            # 상하좌우와 대각선
            if arr[nx][i] or arr[i][nx]:








T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 체스판
    arr = [[0]*N for _ in range(N)]
    for
