import sys
sys.stdin = open("input.txt", "r")
def flag_color(arr):
    result = []
    w_cnt = 0
    b_cnt = 0
    r_cnt = 0

    for i in range(len(arr)):
        if arr[i] != 'W':
            w_cnt += 1
        if arr[i] != 'B':
            b_cnt += 1
        if arr[i] != 'R':
            r_cnt += 1
    result.append(w_cnt)
    result.append(b_cnt)
    result.append(r_cnt)
    return result

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    # 바꿀 갯수
    cnt = 0
    result = []
    # 바뀐 줄의 색깔 표시
    what = [0]*N
    # 갯수 같을때 바꾸는 경우의수 4가지
    # 첫째줄은 흰색 마지막줄은 빨강으로 칠해야함
    for x in range(N):
        if x == 0:
            cnt += flag_color(flag[x])[0]
            what[x] = 'W'
        if x == N-1:
            cnt += flag_color(flag[x])[2]
            what[x] = 'R'
        # 마지막 전줄확인하는데 파란색이 1개도없으면 파랑으로 칠해줘야됨
        elif x == N-2:
            if 'B' not in what:
                cnt += flag_color(flag[x])[1]
                what[x] = 'B'
            else:
                cnt += flag_color(flag[x])[2]
                what[x] = "R"
        # 윗줄이 흰색일 때는 파랑이나 흰색중 작은걸로 칠한다.
        elif what[x-1] == 'W':
            if flag_color(flag[x])[0] <= flag_color(flag[x])[1]:
                what[x] = 'W'
                cnt += flag_color(flag[x])[0]
            elif flag_color(flag[x])[0] > flag_color(flag[x])[1]:
                what[x] = 'B'
                cnt += flag_color(flag[x])[1]
        # 윗줄이 파랑일 때는 파랑과 빨강중 작은걸로 칠한다.
        elif what[x-1] == 'B':
            if flag_color(flag[x])[1] <= flag_color(flag[x])[2]:
                what[x] = 'B'
                cnt += flag_color(flag[x])[1]
            elif flag_color(flag[x])[1] > flag_color(flag[x])[2]:
                what[x] = 'R'
                cnt += flag_color(flag[x])[2]
        # 윗줄이 빨강이면 빨강으로 칠한다.
        elif what[x-1] == 'R':
            what[x] = 'R'
            cnt += flag_color(flag[x])[2]
    result.append(cnt)


    # 바꿀 갯수
    cnt_2 = 0
    # 바뀐 줄의 색깔 표시
    what_2 = [0] * N
    for x in range(N):
        if x == 0:
            cnt_2 += flag_color(flag[x])[0]
            what_2[x] = 'W'
        if x == N-1:
            cnt_2 += flag_color(flag[x])[2]
            what_2[x] = 'R'
        # 마지막 전줄확인하는데 파란색이 1개도없으면 파랑으로 칠해줘야됨
        elif x == N-2:
            if 'B' not in what_2:
                cnt_2 += flag_color(flag[x])[1]
                what_2[x] = 'B'
            else:
                cnt_2 += flag_color(flag[x])[2]
                what_2[x] = "R"
        # 윗줄이 흰색일 때는 파랑이나 흰색중 작은걸로 칠한다.
        elif what_2[x-1] == 'W':
            if flag_color(flag[x])[0] < flag_color(flag[x])[1]:
                what_2[x] = 'W'
                cnt_2 += flag_color(flag[x])[0]
            elif flag_color(flag[x])[0] >= flag_color(flag[x])[1]:
                what_2[x] = 'B'
                cnt_2 += flag_color(flag[x])[1]
        # 윗줄이 파랑일 때는 파랑과 빨강중 작은걸로 칠한다.
        elif what_2[x-1] == 'B':
            if flag_color(flag[x])[1] < flag_color(flag[x])[2]:
                what_2[x] = 'B'
                cnt_2 += flag_color(flag[x])[1]
            elif flag_color(flag[x])[1] >= flag_color(flag[x])[2]:
                what_2[x] = 'R'
                cnt_2 += flag_color(flag[x])[2]
        # 윗줄이 빨강이면 빨강으로 칠한다.
        elif what_2[x-1] == 'R':
            what_2[x] = 'R'
            cnt_2 += flag_color(flag[x])[2]
    result.append(cnt_2)






























