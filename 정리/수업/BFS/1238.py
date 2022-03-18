import sys
sys.stdin = open("input.txt", "r")

def BFS(start):
    Q = []
    visited = [0] * 101
    Q.append(start)
    visited[start] = 1
    # 정답 찾을 거
    sol = start
    while Q:
        now = Q.pop(0)
        # 현재 방문위치가 더 나중에 전화 한거거나
        # 전화받은 순서가 같다면 숫자가 큰사람으로 정답을 바꿔줌
        if visited[sol] < visited[now] or visited[sol] == visited[now] and sol < now:
            sol = now
        try:
            for i in info[f'{now}']:
                # 방문한적 없으면
                if visited[i] == 0:
                    # 전화받는 순서 1 증가시켜서 방문체크
                    visited[i] = visited[now] + 1
                    Q.append(i)
        except:
            continue
    return sol

for tc in range(1, 11):
    long, K = list(map(int,input().split()))
    arr = list(input().split())
    info = dict()
    for i in range(long // 2):
        info[arr[i*2]] = []
    for i in range(long // 2):
        if int(arr[i*2+1]) not in info[arr[i*2]]:
            info[arr[i*2]].append(int(arr[i*2+1]))

    print(f'#{tc} {BFS(K)}')

# 교수님 풀이
# def BFS(s):
#     Q = []
#     visited = [0] * 101
#     Q.append(s)
#     visited[s] = 1
#     # 정답 뽑을거
#     sol = s
#     while Q:
#         now = Q.pop(0)
#         if visited[sol] < visited[now] or visited[sol] == visited[now] and sol < now:
#             sol = now
#         for j in range(1, 101):
#             if adj[now][j] and visited[j] == 0:
#                 Q.append(j)
#                 visited[j] = visited[now] + 1
#     return sol
# for tc in range(1, 11):
#     N, S = map(int, input().split())
#     lst = list(map(int, input().split()))
#     adj = [[0]*101 for _ in range(101)]
#     for i in range(0, len(lst), 2):
#         adj[lst[i]][lst[i+1]] = 1
#     ans = BFS(S)
#     print(f'#{tc} {ans}')