T = int(input())

for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    # 격자 확인
    for i in range(0, 9, 3):      # 기준점은 3칸씩 이동
        for j in range(0, 9, 3):
            numbers = set()
            for k in range(i, i+3):
                for p in range(j, j+3):
                    numbers.add(puzzle[k][p])
            if len(numbers) != 9:
                result = 0
                break
    # 가로 확인
    for i in range(9):
        numbers = set()
        for j in range(9):
            numbers.add(puzzle[i][j])
        if len(numbers) != 9:
            result = 0
            break
    # 세로 확인
    for i in range(9):
        numbers = set()
        for j in range(9):
            numbers.add(puzzle[j][i])
        if len(numbers) != 9:
            result = 0
            break

    if result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')