def pascal(N):
    # N만큼 [1]을 생성
    arr = [1]*N
    # N <= 2일때는 그냥 arr 리턴하면됨
    if N <= 2:
        return arr
    else:
        # N > 2 부터는 arr[0]하고 arr[-1]을 제외하곤 arr의 각 인덱스의 값을
        # pascal(N-1) i-1과 i번째 인덱스의 값의 합으로 바꿔줘야함
        for i in range(1, N-1):
            arr[i] = pascal(N-1)[i-1] + pascal(N-1)[i]
        return arr

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    print(f'#{tc}')
    for i in range(1, N+1):
        print(*pascal(i))
