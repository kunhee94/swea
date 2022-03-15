import sys
sys.stdin = open("input.txt", "r")

# # 시간초과
# # 델타이동 상하좌우
# dx = [0, 0, -0.5, 0.5]
# dy = [0.5, -0.5, 0, 0]
#
# T = int(input())
#
# for tc in range(1, 1+T):
#     N = int(input())
#     info = [list(map(int, input().split())) for _ in range(N)]
#     result = 0
#
#
#     # info =[x좌표 y 좌표 방향 에너지]
#     # 전부 다 쌍소멸될때까지 반복
#     cnt = 0
#     while info:
#         cnt += 1
#         for i in info:
#             i[0] += dx[i[2]]
#             i[1] += dy[i[2]]
#         # 2000번이상 시행했는데 아직도 쌍소멸안된거는 안만나는것들만 남은거
#         if cnt > 2000:
#             break
#         # 쌍소멸 명단
#         delete = set()
#         # 딕셔너리로 갯수를 셀까?
#         mach = dict()
#         for i in info:
#             mach[f'{[i[0], i[1]]}'] = 0
#         for i in info:
#             mach[f'{[i[0], i[1]]}'] += 1
#         # 벨류값이 2이상이면 쌍소멸 명단
#         for i in mach.items():
#             if i[1] >= 2:
#                 delete.add(i[0])
#         # 벨류값 2이상 없으면 바로 다시 while문 돌아야함
#         if len(mach) == 0:
#             continue
#         # info 다시 돌면서 소멸할 애들 소멸시키고 에너지 계산
#         k = info[:]
#         for i in info:
#             if f'{[i[0], i[1]]}' in delete:
#                 result += i[3]
#                 k.remove(i)
#         info = k
#     print(f'#{tc} {result}')




# # 델타이동 상하좌우
# dx = [0, 0, -0.5, 0.5]
# dy = [0.5, -0.5, 0, 0]
#
# T = int(input())
#
# for tc in range(1, 1+T):
#     N = int(input())
#     info = [list(map(int, input().split())) for _ in range(N)]
#     result = 0
#     k = info[:]
#     # 가망없는 친구들 삭제
#     for i in range(N):
#         # 방향이 0 일때
#         if info[i][2] == 0:
#             for j in range(N):
#                 # 방향이 1이고 x좌표가 동일한 info가 있는지 체크
#                 if info[i][0] == info[j][0] and info[j][2] == 1:
#                     break
#             # 없었다면 info[i]삭제해야함
#             else:
#                 k.remove(info[i])
#         # 방향 1 일 때
#         elif info[i][2] == 1:
#             for j in range(N):
#                 # 방향이 0이고 x좌표가 동일한 info가 있는지 체크
#                 if info[i][0] == info[j][0] and info[j][2] == 0:
#                     break
#             # 없었다면 info[i]삭제해야함
#             else:
#                 k.remove(info[i])
#         # 방향 2 일 때
#         elif info[i][2] == 2:
#             for j in range(N):
#                 # 방향이 3이고 y좌표가 동일한 info가 있는지 체크
#                 if info[i][1] == info[j][1] and info[j][2] == 3:
#                     break
#             # 없었다면 info[i]삭제해야함
#             else:
#                 k.remove(info[i])
#         # 방향 3 일 때
#         elif info[i][2] == 3:
#             for j in range(N):
#                 # 방향이 2이고 y좌표가 동일한 info가 있는지 체크
#                 if info[i][1] == info[j][1] and info[j][2] == 2:
#                     break
#             # 없었다면 info[i]삭제해야함
#             else:
#                 k.remove(info[i])
#     info = k
#     p = info[:]
#     # 쌍소멸 과정
#     i = 0
#     while p:
#         # 방향이 0 일때
#         if info[i][2] == 0:
#             for j in range(N):
#                 # 방향이 1이고 x좌표가 동일한 info 체크
#                 if info[i][0] == info[j][0] and info[j][2] == 1:
#                     # 에너지 계산
#                     result += info[i][3]
#                     result += info[j][3]
#                     p.remove(info[i])
#                     p.remove(info[j])
#         # 방향 1 일 때
#         elif info[i][2] == 1:
#             for j in range(N):
#                 # 방향이 0이고 x좌표가 동일한 info 체크
#                 if info[i][0] == info[j][0] and info[j][2] == 0:
#                     # 에너지 계산
#                     result += info[i][3]
#                     result += info[j][3]
#                     p.remove(info[i])
#                     p.remove(info[j])
#         # 방향 2 일 때
#         elif info[i][2] == 2:
#             for j in range(N):
#                 # 방향이 3이고 y좌표가 동일한 info가 있는지 체크
#                 if info[i][1] == info[j][1] and info[j][2] == 3:
#                     # 에너지 계산
#                     result += info[i][3]
#                     result += info[j][3]
#                     p.remove(info[i])
#                     p.remove(info[j])
#         # 방향 3 일 때
#         elif info[i][2] == 3:
#             for j in range(N):
#                 # 방향이 2이고 y좌표가 동일한 info가 있는지 체크
#                 if info[i][1] == info[j][1] and info[j][2] == 2:
#                     # 에너지 계산
#                     result += info[i][3]
#                     result += info[j][3]
#                     p.remove(info[i])
#                     p.remove(info[j])
#
#     print(f'#{tc} {result}')


# 또 틀려?
# 델타이동 상하좌우
dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    k = info[:]
    # 가망없는 친구들 삭제
    for i in range(N):
        # 방향이 0 일때
        if info[i][2] == 0:
            for j in range(N):
                # 방향이 1이고 x좌표가 동일한 info가 있는지 체크
                if info[i][0] == info[j][0] and info[j][2] == 1:
                    break
            # 없었다면 info[i]삭제해야함
            else:
                k.remove(info[i])
        # 방향 1 일 때
        elif info[i][2] == 1:
            for j in range(N):
                # 방향이 0이고 x좌표가 동일한 info가 있는지 체크
                if info[i][0] == info[j][0] and info[j][2] == 0:
                    break
            # 없었다면 info[i]삭제해야함
            else:
                k.remove(info[i])
        # 방향 2 일 때
        elif info[i][2] == 2:
            for j in range(N):
                # 방향이 3이고 y좌표가 동일한 info가 있는지 체크
                if info[i][1] == info[j][1] and info[j][2] == 3:
                    break
            # 없었다면 info[i]삭제해야함
            else:
                k.remove(info[i])
        # 방향 3 일 때
        elif info[i][2] == 3:
            for j in range(N):
                # 방향이 2이고 y좌표가 동일한 info가 있는지 체크
                if info[i][1] == info[j][1] and info[j][2] == 2:
                    break
            # 없었다면 info[i]삭제해야함
            else:
                k.remove(info[i])
    # 쌍소멸될 명단만 남음 에너지 다 더하면됨
    info = k
    for i in info:
        result += i[3]

    print(f'#{tc} {result}')




