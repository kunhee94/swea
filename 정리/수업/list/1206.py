#min 함수를 만듬
def my_min(a):
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    return a[-1]
#테스트 케이스 = 10  테스트케이스만큼 출력해야됨
for tc in range(1,11):
    T = int(input())        #빌딩 부지 수
    bds = list(map(int,input().split()))  #각 부지에 빌딩 높이
    total = 0                             #조망권 확보된 세대 합
    for i in range(2, len(bds[0:-2])):    #앞뒤 인덱스 2개는 0이므로 2부터 끝에서 3번째 까지만 인덱스 돌리면됨
        if bds[i]-bds[i-2] >= 1 and bds[i]-bds[i-1] >= 1 and bds[i]-bds[i+1] >= 1 and bds[i]-bds[i+2] >= 1:
            #양 옆 2개의 빌딩 높이가 일단 무조건 자기보다 낮아야함
            l_bds = [bds[i]-bds[i-2], bds[i]-bds[i-1], bds[i]-bds[i+1], bds[i]-bds[i+2]]
            total += my_min(l_bds)
            # 그중에서 차이가 가장 작은 빌딩과의 차이가 조망권 확보된 세대 수임
    print(f'#{tc} {total}')