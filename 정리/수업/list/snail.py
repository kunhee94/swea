T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list([0]*N for _ in range(N))
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    r, c = 0, 0         # 최초좌표
    m_rc = 0            # 0123 순서로 우하좌상
    for i in range(1,N**2+1):  # N제곱만큼 숫자 뽑아야됨
        arr[c][r] = i
        c += dc[m_rc]          #우선 오른쪽으로 가면서 1,2,3,이렇게 넣어줌
        r += dr[m_rc]
        if r < 0 or c < 0 or r > N-1 or c > N-1 or arr[c][r] != 0:
            # 그러다가 인덱스에서 벗어나거나 그자리에 숫자가 이미 채워져있다면?
            c -= dc[m_rc]      # 일단 증가시킨 c,r 원상복귀
            r -= dr[m_rc]
            m_rc = (m_rc+1)%4   #우하좌상 순으로 움직임 바꿔줘야함
            c += dc[m_rc]       #그리고 c r 다시 움직여주고 for문 돌림
            r += dr[m_rc]
    print(f"#{tc}")
    for i in arr:
        print(*i)       # arr을 돌면서 내부 리스트 언패킹해서 출력