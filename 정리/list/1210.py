for i in range(10):
    tc = int(input())
    # 사다리
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):  # 99행에서 2값의 위치 찾기
        if arr[99][i] == 2:
            c = i

    dr = [-1, 0, 0]  # 상우좌 순서
    dc = [0, 1, -1]
    r = 99
    # arr[99][c]부터 시작
    while r > 0:    # r이 0일때의 c값이 필요함
        where = []  # 방향 어디로 갈지 정할 리스트
        for k in range(3):  # 3방향 확인
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 100 and 0 <= nc < 100:
                if arr[nr][nc] == 1:    # 이동할 위치에 1이 있으면 1을 where에 저장
                    where.append(1)
                else:
                    where.append(0)     # 없으면 0을 저장
            else:
                where.append(0)     # 만약 인덱스 범위를 벗어나도 0 저장

        # 이제 실제로 움직일 건데 움직일 때마다 원래 있던 위치를 1이 아닌
        # 2로 바꿔준다 (좌우 모두 1일때 어디로 가야할지 정해줘야하니까)
            # 양옆이 모두 1이 아닐 때만 위로감
        if where == [1, 0, 0]:
            arr[r][c] = 2
            r += dr[0]
            # 위와 우가 1이거나 우만 1일경우에 우로감
        elif where == [1, 1, 0] or where == [0, 1, 0]:
            arr[r][c] = 2
            c += dc[1]
            # 위와 좌가 1이거나 좌만 1일경우에 좌로감
        elif where == [1, 0, 1] or where == [0, 0, 1]:
            arr[r][c] = 2
            c += dc[2]

    print(f'#{tc} {c}')