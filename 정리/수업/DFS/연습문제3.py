import sys
sys.stdin = open("input.txt", "r")

nc, ec = map(int, input().split())      # 노드갯수, 간선갯수
edges = list(map(int, input().split()))

# 방문 경로를 저장할 2차원 리스
G = [[0] * (nc+1) for _ in range(nc+1)]
# G[출발점][도착점] = 1로 만들어서 방문경로를 저장
# 방향이 없으니 양방향으로 갈수 있다 그래서
# G[도착점][출발점] = 1도 해줘야한다

for idx in range(ec):
    # edges[idx*2] 출발점, edges[idx*2+1] 도착점
    G[edges[idx*2]][edges[idx*2 + 1]] = 1
    G[edges[idx*2 + 1]][edges[idx*2]] = 1

visited = [False] * (nc + 1)
start = edges[0]      # 1부터 시작
stack = [start]

while stack:
    now = stack.pop()     # 현재 방문하고 있는 지점

    if visited[now] == 0:   # 방문한적 없는지 확인
        visited[now] = True     # 방문으로 수정
        print(now, end=' ')     # 방문 지점 출력

        # 다음 갈 수 있는 노드를 탐색 => G에 인접 노드 정보가 들어있다.
        # G[출발][도착] == 1이면 이동가능한 노드
        for nxt in range(nc, -1, -1):
            if G[now][nxt] == 1 and visited[nxt] == 0:
                stack.append(nxt)


