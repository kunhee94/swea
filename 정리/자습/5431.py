
T = int(input())

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    a = [i for i in range(1, N+1)]
    result = []
    jechull = list(map(int, input().split()))
    for i in a:
        if i not in jechull:
            result.append(i)
    print(f'#{tc}', *result)
