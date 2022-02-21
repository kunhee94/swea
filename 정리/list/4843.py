T = int(input())
# 1번째로 큰수, 1번째로 작은수,2번째로 큰수 2번째로 작은수...로 정렬
# 10개만 하면됨

# 선택정렬
def select_(arr, N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1,N):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr

for tc in range(1, T+1):
    N = int(input())    # 숫자갯수
    N_list = list(map(int, input().split()))
    sort_list = select_(N_list, N)
    spacial = []
    for i in range(10):
        if i%2==0:      # 짝수번째에는 최대
            spacial.append(sort_list[-1])
            sort_list.remove(sort_list[-1]) # 뽑고 다음 최대 찾아야되니까 기존 최대 삭제
        else:           # 홀수번째에는 최소
            spacial.append(sort_list[0])
            sort_list.remove(sort_list[0])  # 뽑고 다음 최소 찾아야되니까 기존 최소 삭제
    print(f'#{tc}', end=" ")
    for i in spacial:
        print(i, end=" ")
    print()
