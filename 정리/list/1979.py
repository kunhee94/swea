# 1이 연속된다면 그 길이값 리스트 반환
def how_many(arr):
    cnt_list = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i]:
            cnt += 1
            if i == len(arr)-1:
                cnt_list.append(cnt)
        else:
            cnt_list.append(cnt)
            cnt = 0
    return cnt_list

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 전치 행렬
    arr2 = list(map(list, (zip(*arr))))
    cnt = 0
    for i in range(N):
        for j in how_many(arr[i]):
            if j == K:
                cnt += 1
    for i in range(N):
        for j in how_many(arr2[i]):
            if j == K:
                cnt += 1
    print(f'#{tc} {cnt}')