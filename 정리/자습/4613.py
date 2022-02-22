import sys
sys.stdin = open("input.txt", "r")

# def flag_color(arr):
#     M = len(arr)
#     result = []
#     cnt = 0
#     for y in range(M):
#         if arr[y] != 'W':
#             cnt += 1
#     result.append(cnt)
#     cnt = 0
#     for y in range(M):
#         if arr[y] != 'B':
#             cnt += 1
#     result.append(cnt)
#     cnt = 0
#     for y in range(M):
#         if arr[y] != 'R':
#             cnt += 1
#     result.append(cnt)
#     return result
#
# T = int(input())
#
# for tc in range(1, 1+T):
#     N, M = map(int, input().split())
#     flag = [list(map(str, input())) for _ in range(N)]
#     cnt = 0
#
#     # 첫번째 줄이거나 위의 줄이 흰색이었고 흰색바꿀때 횟수가
#     # 가장 작을때는 cnt에 flag_color(flag)[0]을 더해줌
#     for i in range(N):
#         # 첫번째 줄은 흰색으로 칠한다.
#         if i == 0:
#             flag[i][0] = 'W'
#             cnt += flag_color(flag[i])[0]
#
#         # 윗줄이 흰줄이고 흰색으로 바꿀 때 횟수가 파랑으로 바꿀때 보다 작거나 같으면 흰색으로 칠함
#         elif flag[i-1][0] == 'W':
#             # flag_color(flag[i])[0] < flag_color(flag[i])[1] 이러면 흰색 횟수가 적은거
#             if flag_color(flag[i])[0] <= flag_color(flag[i])[1]:
#                 flag[i][0] = 'W'
#                 cnt += flag_color(flag[i])[0]
#
#         # 윗줄이 흰줄이고 파랑으로 바꿀 때 횟수가 흰색으로 바꿀때 보다 작거나 같다면 파랑으로 칠함
#         elif flag[i-1][0] == 'W':
#             if flag_color(flag[i])[1] < flag_color(flag[i])[0]:
#                 flag[i][0] = 'B'
#                 cnt += flag_color(flag[i])[1]
#
#         # 윗줄이 파랑이고 파랑으로 바꿀 때 횟수가 빨강으로 바꿀때 보다 작다면 파랑으로 칠함
#         elif flag[i-1][0] == 'B':
#             if flag_color(flag[i])[1] < flag_color(flag[i])[2]:
#                 flag[i][0] = 'B'
#                 cnt += flag_color(flag[i])[1]
#
#         # 윗줄이 파랑이고 빨강으로 바꿀 때 횟수가 파랑으로 바꿀때 보다 작다면 빨강으로 칠함
#         elif flag[i-1][0] == 'B':
#             if flag_color(flag[i])[2] < flag_color(flag[i])[1]:
#                 flag[i][0] = 'R'
#                 cnt += flag_color(flag[i])[2]
#
#         # 윗줄이 빨강이면 빨강으로 칠함
#         elif flag[i-1][0] == 'R':
#             cnt += flag_color(flag[i])[2]
#
#         # 마지막줄은 빨강이어야 함
#         elif i == N-1:
#             cnt += flag_color(flag[i])[2]
#     print(cnt)




def flag_color(arr):
    M = len(arr)
    result = []
    cnt = 0
    for y in range(M):
        if arr[y] != ['W']:
            cnt += 1
    result.append(cnt)
    cnt = 0
    for y in range(M):
        if arr[y] != ['B']:
            cnt += 1
    result.append(cnt)
    cnt = 0
    for y in range(M):
        if arr[y] != ['R']:
            cnt += 1
    result.append(cnt)
    return result

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    flag = [list(map(list, input())) for _ in range(N)]

    cnt = flag_color(flag[0])[0]
    flag[0][0] = ['W']

    # 첫번째 줄이거나 위의 줄이 흰색이었고 흰색바꿀때 횟수가
    # 가장 작을때는 cnt에 flag_color(flag)[0]을 더해줌
    for i in range(1, N):
        # 윗줄이 흰줄이고 흰색으로 바꿀 때 횟수가 파랑으로 바꿀때 보다 작거나 같으면 흰색으로 칠함
        if flag[i-1][0] == ['W'] and flag_color(flag[i])[0] <= flag_color(flag[i])[1]:
            flag[i][0] = ['W']
            cnt += flag_color(flag[i])[0]

        # 윗줄이 흰줄이고 파랑으로 바꿀 때 횟수가 흰색으로 바꿀때 보다 작으면 파랑으로 칠함
        elif flag[i-1][0] == ['W'] and flag_color(flag[i])[1] < flag_color(flag[i])[0]:
            flag[i][0] = ['B']
            cnt += flag_color(flag[i])[1]

        # 윗줄이 파랑이고 파랑으로 바꿀 때 횟수가 빨강으로 바꿀때 보다 작다면 파랑으로 칠함
        elif flag[i-1][0] == ['B'] and flag_color(flag[i])[1] < flag_color(flag[i])[2]:
            flag[i][0] = ['B']
            cnt += flag_color(flag[i])[1]

        # 윗줄이 파랑이고 빨강으로 바꿀 때 횟수가 파랑으로 바꿀때 보다 작거나 같다면 빨강으로 칠함
        elif flag[i-1][0] == ['B'] and flag_color(flag[i])[2] <= flag_color(flag[i])[1]:
            flag[i][0] = ['R']
            cnt += flag_color(flag[i])[2]

        # 윗줄이 빨강이면 빨강으로 칠함
        elif flag[i-1][0] == ['R']:
            cnt += flag_color(flag[i])[2]

        # 마지막줄은 빨강이어야 함
        elif i == N-1:
            cnt += flag_color(flag[i])[2]
    print(cnt)

































