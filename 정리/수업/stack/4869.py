T = int(input())

# paper(10) = 1
# paper(20) = 3
# 그 뒤로는 paper(N) = paper(N-20)*2 + paper(N-10)의 규칙성이 있음
def paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return paper(N-20)*2 + paper(N-10)


for tc in range(1, 1+T):
    N = int(input())
    print(f'#{tc} {paper(N)}')
