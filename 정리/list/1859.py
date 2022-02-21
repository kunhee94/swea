def my_max(a):
    result = 0
    for i in range(len(a)):
        if result < a[i]:
            result = a[i]
    return result

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = my_max(price)   # 제일 비싼가격
    result = 0
    for idx in range(N-1):
        if price[idx] == max_price:
            max_price = my_max(price[idx+1:])
        elif price[idx] < max_price:
            result += max_price - price[idx]
    print(f'#{tc} {result}')

# 최적화 했는데도 에러뜸 swea 문제인듯
T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    price = list(map(int, input().split()))
    m_price = max(price)
    result = 0
    for i in range(len(price)-1):
        if price[i] < m_price:
            result += (m_price - price[i])
        elif price[i] >= m_price:
            m_price = max(price[i+1:len(price)])
    print(f'#{tc} {result}')