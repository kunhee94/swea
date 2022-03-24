import sys
sys.stdin =open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, num = input().split()
    N = int(N)
    bit = ''
    for i in range(N):
        bit += f'{int(num[i], base=16):04b}'
    print(f'#{tc} {bit}')
