T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    ch_st = [0]*(N+1)              # 충전기가 있는 정류장
    for i in range(N+1):
        for j in charge:
            if i == j:
                ch_st[i] = 1
    bus_pt = 0                      # 버스 위치
    ch_cnt = 0                       # 충전 횟수
    while True:
        bus_pt += K                 # 먼저 K만큼 버스이동
        if bus_pt >= N:             # 종점 도착 시 while문 종료
            break
        for i in range(bus_pt, bus_pt-K, -1): # 버스가 이동한 위치부터 하나씩 뒤로 가면서 충전소 유무 확인
            if ch_st[i] == 1:           # i = 버스위치
                ch_cnt += 1             # i에 충전소가 있다면
                bus_pt = i              # 충전 횟수 늘리고 버스를 i로 이동 확정
                break                   # for문을 나옴
        else:                           # 노선설계 실수로 종점이동 불가능한 경우 0을 출력해야 함
            ch_cnt = 0
            break
    print(f'#{tc} {ch_cnt}')

# 다시 풀어봄
T = int(input())

for tc in range(1,1+T):
    K, N, M = map(int, input().split())
    charge_st = list(map(int, input().split()))
    bus_st = [0]*(N+1)
    # 어느 정류장에 충선소 있는지 표시
    for i in range(len(charge_st)):
        bus_st[charge_st[i]] += 1
    bus = K         # 버스 위치
    ch_cnt = 0      # 충전 횟수
    a = 0           # 이동위치에 충전기 없을때 뒤로 돌아가는 횟수
    while True:
        if bus >= N:
            break
        if bus_st[bus]:
            bus += K
            ch_cnt += 1
            a = 0
        else:
            bus -= 1
            a += 1
            if a == K:  # K만큼 뒤로 돌아가야 한다면 노선 설계문제임
                ch_cnt = 0
                break
    print(f'#{tc} {ch_cnt}')