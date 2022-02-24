T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dx = [-1, 0, 1, 0]      # 상우하좌 순
    dy = [0, 1, 0, -1]
    start_x = 0
    start_y = 0
    stack_x = []
    stack_y = []
    # 츌발점찾기
    for a in range(N):
        for b in range(N):
            # 2면 출발점임
            if miro[a][b] == 2:
                start_x = a
                start_y = b
                stack_x.append(a)
                stack_y.append(b)
    now_x, now_y = start_x, start_y
    while miro[now_x][now_y] != 3:
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            # 인덱스 범위 안쪽만 탐색
            if 0 <= nx < N and 0 <= ny < N:
                # 길이 있고 방문한적 없다면
                if (miro[nx][ny] == 0 or miro[nx][ny] == 3) and visited[nx][ny] == 0:
                    # 현재 위치에 방문록 적고
                    visited[now_x][now_y] = 5
                    # 현재 위치 스택에 기록
                    stack_x.append(now_x)
                    stack_y.append(now_y)
                    # 이동
                    now_x, now_y = nx, ny
                    break
        # 길이 없거나 방문했을시 이전으로 돌아감
        else:
            # 현재 위치에 방문 표시하고
            visited[now_x][now_y] = 5
            # 이전으로 이동
            now_x, now_y = stack_x.pop(), stack_y.pop()
        # 스택이 비면 출구없는거임 0 출력
        if stack_x == []:
            print(f'#{tc} 0')
            break
    # 출구 찾아서 정상종료 되었으면 1출력
    else:
        print(f'#{tc} 1')
