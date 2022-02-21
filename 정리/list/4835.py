# min,max함수 구현
def my_max(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    return num[-1]

def my_min(num):
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    return num[-1]
# sum함수 구현
def my_sum(num):
    total = 0
    for i in range(len(num)):
        total += num[i]
    return total

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    a = []    # 각 리스트의 M개씩 리스트를 만들어서 담을 곳
    sum_list = []  # M개씩 더한값들의 리스트
    for i in range(N-M+1):      # N-M까지만 돌면됨
        for j in range(i, i+M):  # 다시 i부터 i+M전까지 더할 값들을 구함
            a.append(num_list[j])   # num_list[j]를 a에 더해줌
        sums = my_sum(a)           # a의 합을 sums에 저장
        sum_list.append(sums)      # 더한 sums를 sum_list에 저장
        a = []                     #a는 초기화
    gap = my_max(sum_list) - my_min(sum_list) # max,min에 각각 sum_list 돌림
    print(f'#{tc} {gap}')