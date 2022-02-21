def my_max(a):
    result = 0
    for i in range(len(a)):
        if result < a[i]:
            result = a[i]
    return result

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sums = 0
            for k in range(i, i+M):
                for p in range(j, j+M):
                    sums += arr[k][p]
            result.append(sums)

    print(f'#{tc} {my_max(result)}')