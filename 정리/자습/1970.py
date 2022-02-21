
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0]*8     # 화폐 종류만큼 리스트 미리 생성
    while N > 0:
        if N >= 50000:
            arr[0] += 1
            N -= 50000
        elif N >= 10000:
            arr[1] += 1
            N -= 10000
        elif N >= 5000:
            arr[2] += 1
            N -= 5000
        elif N >= 1000:
            arr[3] += 1
            N -= 1000
        elif N >= 500:
            arr[4] += 1
            N -= 500
        elif N >= 100:
            arr[5] += 1
            N -= 100
        elif N >= 50:
            arr[6] += 1
            N -= 50
        elif N >= 10:
            arr[7] += 1
            N -= 10
        else:
            break
    print(f'#{tc}')
    print(*arr)