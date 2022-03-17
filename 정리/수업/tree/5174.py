import sys
sys.stdin = open("input.txt","r")



def count_nod(n):
    global cnt
    if n:
        cnt += 1
        count_nod(ch1[n])
        count_nod(ch2[n])


T = int(input())

for tc in range(1,T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 0
    count_nod(N)
    print(f'#{tc} {cnt}')

