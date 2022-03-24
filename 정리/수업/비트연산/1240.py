import sys
sys.stdin = open('input.txt', 'r')

pat = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input()for _ in range(N)]
    target = ''
    for password in arr:
        # 어차피 값이 있는 1줄만 읽으면됨
        if int(password):
            target = password
            break
    # 홀수 짝수 확인 편하기 위해서 0번 인덱스 채워두기
    res = [0]
    i = 0
    now = 0
    while i < len(target):
        # 왼쪽부터 7칸씩 패턴이 있는지 확인
        if target[i:i + 7] in pat:
            # 있으면 키값 res에 추가해주고
            res.append(pat[target[i:i + 7]])
            # 현재위치 저장해두기
            if len(res) == 2:
                now = i
            # 7칸 이동
            i += 7
        else:
            # 패턴일치 안했으면 다음칸으로 이동해서 확인
            i += 1
            # 마지막 인덱스까지 체크했는데 res가 9개가 아니면 잘못된 곳에서 찾았단 소리니까
            # 다시 now+1부터 확인
            if i == len(target) - 7 and len(res) != 9:
                i = now + 2
    print(res)
    # 홀수
    hol = 0
    # 짝수
    jjack = 0
    # 7번인덱스까지 확인
    for i in range(8):
        # 홀수
        if i % 2:
            hol += res[i]
        # 짝수면
        else:
            jjack += res[i]
    # 암호코드 검증
    if (hol*3 + jjack + res[-1]) % 10 == 0:
        print(f'#{tc} {sum(res)}')
    else:
        print(f'#{tc} 0')

