import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = input().split()
    for _ in range(M):
        arr.append(arr.pop(0))
    print(f'#{tc} {arr[0]}')