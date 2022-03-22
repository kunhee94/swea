import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    CI = list(map(int, input().split()))
    pizza = []
    for i in range(M):
        # 피자번호와 치즈양 저장
        pizza.append([i+1, CI[i]])
    # N개까지만 화덕에 넣을 수 있다
    Q = pizza[:N]
    # 넣을려면 줄서기
    dagi = pizza[N:]

    while len(Q) > 1:  # 1개만 남으면 중단해야됨
        now = Q.pop(0)  # 피자 다넣고 처음으로 꺼내서 치즈확인
        now[1] = now[1]//2  # 치즈 일단 절반으로 감소
        if now[1] == 0:
            if dagi:
                # 대기중인 피자가있다면 넣어준다
                Q.append(dagi.pop(0))
        else:
            # 다시 넣기
            Q.append(now)
    print(f'#{tc} {Q[0][0]}')


