def check_min_val(x, sum_val):
    global min_val

    if x == N:  # 모든 숫자를 뽑은 경우
        if min_val > sum_val:
            min_val = sum_val
        return

    # 만약 다 더해보기도 전에 구해져있는 최솟값보다 크면 그 아래는 유망하지 않으니 버림
    elif sum_val > min_val:
        return
    else:
        for y in range(N):
            if selected[y] == 0:   # 다른 행에서 뽑힌 적이 없는 열인지 확인
                selected[y] = 1    # 응 내가 그럼 뽑을게
                check_min_val(x + 1, sum_val + arr[x][y])  # 다음 행으로 이동, 선택된 값을 더해줌
                selected[y] = 0    # 고마워 잘 썼어
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    selected = [0] * N
    min_val = 9876543210

    check_min_val(0, 0)   # 시작 row와  더하는 변수 0으로 전달

    print(f'#{tc} {min_val}')