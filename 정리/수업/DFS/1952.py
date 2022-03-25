import sys
sys.stdin = open("input.txt", "r")



def DFS(n, s):
    global res
    if n > 12:
        if res > s:
            res = s
        return
    DFS(n+1, s + arr[n] * day)
    DFS(n+1, s + mon)
    DFS(n+3, s + mon3)
    DFS(n+12, s + year)



T = int(input())

for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    # print(arr)
    res = 9999999999
    DFS(1, 0)
    print(f'#{tc} {res}')