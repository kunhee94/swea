### 1206번

```python
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

```

### 1208번

```python
def my_max(num):
    max_ = num[0]
    for i in range(len(num)):
        if num[i] > max_:
            max_ = num[i]
    return max_

def my_min(num):
    min_ = num[0]
    for i in range(len(num)):
        if num[i] < min_:
            min_ = num[i]
    return min_

def max_idx(a):
    for i in range(len(a)):
        if a[i] == my_max(a):
            return i

def min_idx(a):
    for i in range(len(a)):
        if a[i] == my_min(a):
            return i

for tc in range(1,11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    dump_cnt = 0
    while dump_cnt < dump:              # dump 크기만큼 실행해야함
        if boxes[max_idx(boxes)]-boxes[min_idx(boxes)] == 0 or boxes[max_idx(boxes)]-boxes[min_idx(boxes)] == 1:
            break                       # 만약 덤프중에 평탄화 끝나면 while문 빠져나오기
        boxes[max_idx(boxes)] -= 1      # 기존 최고높이의 상자의 인덱스를 찾아내서 boxes의 해당 인덱스의 값을 1 줄임
        boxes[min_idx(boxes)] += 1      # 기존 최저높이의 상자의 인덱스를 찾아내서 boxes의 해당 인덱스의 값을 1 늘림
        dump_cnt += 1
    print(f'#{tc} {boxes[max_idx(boxes)]-boxes[min_idx(boxes)]}')
```

### 4834번

```python
def my_max(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    return num[-1]

def my_count(a,k):
    cnt = 0
    for i in a:
        if i == k:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cards =list(map(int,input()))
    result = {} # 카드와 카드장수를 딕셔너리 형식으로 담을것
    # cards를 돌면서 {카드숫자:카드갯수}딕셔너리를 만들어서 result에 저장
    for card in cards:
        result[card]= my_count(cards,card)
    max_card = []   # result의 밸류값 모음

    for i in result:
        max_card.append(result[i])   # 밸류값들을 max_card에 저장
    ks = []                          # 가장 많은 카운트를 가진 키들의 목록
    for i in result:
        if result[i] == my_max(max_card):
            ks.append(i)
    m = my_max(ks)                  # ks 중 에서 가장 큰 값을 가진 키를 찾는다.
    print(f'#{tc} {m} {result[m]}') # 출력
```

### 4835번

```python
# min,max함수 구현
def my_max(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    return num[-1]

def my_min(num):
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    return num[-1]
# sum함수 구현
def my_sum(num):
    total = 0
    for i in range(len(num)):
        total += num[i]
    return total

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    a = []    # 각 리스트의 M개씩 리스트를 만들어서 담을 곳
    sum_list = []  # M개씩 더한값들의 리스트
    for i in range(N-M+1):      # N-M까지만 돌면됨
        for j in range(i, i+M):  # 다시 i부터 i+M전까지 더할 값들을 구함
            a.append(num_list[j])   # num_list[j]를 a에 더해줌
        sums = my_sum(a)           # a의 합을 sums에 저장
        sum_list.append(sums)      # 더한 sums를 sum_list에 저장
        a = []                     #a는 초기화
    gap = my_max(sum_list) - my_min(sum_list) # max,min에 각각 sum_list 돌림
    print(f'#{tc} {gap}')
```

### 4831번

```python
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
```

### 달팽이

```python
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
```

### 1210 사다리

```python
for i in range(10):
    tc = int(input())
    # 사다리
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):  # 99행에서 2값의 위치 찾기
        if arr[99][i] == 2:
            c = i

    dr = [-1, 0, 0]  # 상우좌 순서
    dc = [0, 1, -1]
    r = 99
    # arr[99][c]부터 시작
    while r > 0:    # r이 0일때의 c값이 필요함
        where = []  # 방향 어디로 갈지 정할 리스트
        for k in range(3):  # 3방향 확인
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 100 and 0 <= nc < 100:
                if arr[nr][nc] == 1:    # 이동할 위치에 1이 있으면 1을 where에 저장
                    where.append(1)
                else:
                    where.append(0)     # 없으면 0을 저장
            else:
                where.append(0)     # 만약 인덱스 범위를 벗어나도 0 저장

        # 이제 실제로 움직일 건데 움직일 때마다 원래 있던 위치를 1이 아닌
        # 2로 바꿔준다 (좌우 모두 1일때 어디로 가야할지 정해줘야하니까)
            # 양옆이 모두 1이 아닐 때만 위로감
        if where == [1, 0, 0]:
            arr[r][c] = 2
            r += dr[0]
            # 위와 우가 1이거나 우만 1일경우에 우로감
        elif where == [1, 1, 0] or where == [0, 1, 0]:
            arr[r][c] = 2
            c += dc[1]
            # 위와 좌가 1이거나 좌만 1일경우에 좌로감
        elif where == [1, 0, 1] or where == [0, 0, 1]:
            arr[r][c] = 2
            c += dc[2]

    print(f'#{tc} {c}')
```

### 4843번

```python
T = int(input())
# 1번째로 큰수, 1번째로 작은수,2번째로 큰수 2번째로 작은수...로 정렬
# 10개만 하면됨

# 선택정렬
def select_(arr, N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1,N):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr

for tc in range(1, T+1):
    N = int(input())    # 숫자갯수
    N_list = list(map(int, input().split()))
    sort_list = select_(N_list, N)
    spacial = []
    for i in range(10):
        if i%2==0:      # 짝수번째에는 최대
            spacial.append(sort_list[-1])
            sort_list.remove(sort_list[-1]) # 뽑고 다음 최대 찾아야되니까 기존 최대 삭제
        else:           # 홀수번째에는 최소
            spacial.append(sort_list[0])
            sort_list.remove(sort_list[0])  # 뽑고 다음 최소 찾아야되니까 기존 최소 삭제
    print(f'#{tc}', end=" ")
    for i in spacial:
        print(i, end=" ")
    print()

```

### 1216 회문

```python
def my_max(a):
    result = 0
    for i in range(len(a)):
        if result < a[i]:
            result = a[i]
    return result

def mk_reverse(a):
    return a[::-1]

for tc in range(1, 11):
    garbage = input()
    arr = [input()for _ in range(100)]
    len_list = []
    # 전치행렬 만들기
    arr2 = list(zip(*arr))  # zip로 전치해준다
    arr2_str = []  # 전치해서 지금 튜플로 들어가있으니 문자열로바꿔서 리스트로 저장
    for i in arr2:
        sero_str = ''
        for j in i:
            sero_str += j
        arr2_str.append(sero_str)
    # 가로와 세로 판단 회문 시작
    for i in range(100):
        for j in range(100):       # arr[0~99][0~99:1~100]을 전부 확인 해본다
            for k in range(j+1, 101):
                if arr[i][j:k] == mk_reverse(arr[i][j:k]):
                    len_list.append(len(arr[i][j:k]))
                if arr2_str[i][j:k] == mk_reverse(arr2_str[i][j:k]):
                    len_list.append(len(arr2_str[i][j:k]))

    print(f'#{tc} {my_max(len_list)}')
```

### 2001 파리퇴치

```python
def my_max(a):
    result = 0
    for i in range(len(a)):
        if result < a[i]:
            result = a[i]
    return result

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sums = 0
            for k in range(i, i+M):
                for p in range(j, j+M):
                    sums += arr[k][p]
            result.append(sums)

    print(f'#{tc} {my_max(result)}')
```

### 1979번

```python
# 1이 연속된다면 그 길이값 리스트 반환
def how_many(arr):
    cnt_list = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i]:
            cnt += 1
            if i == len(arr)-1:
                cnt_list.append(cnt)
        else:
            cnt_list.append(cnt)
            cnt = 0
    return cnt_list

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 전치 행렬
    arr2 = list(map(list, (zip(*arr))))
    cnt = 0
    for i in range(N):
        for j in how_many(arr[i]):
            if j == K:
                cnt += 1
    for i in range(N):
        for j in how_many(arr2[i]):
            if j == K:
                cnt += 1
    print(f'#{tc} {cnt}')
```

### 1974번

```python
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
```

### 5356번

```python
def my_max(a):
    result = 0
    for i in range(len(a)):
        if result < a[i]:
            result = a[i]
    return result
T = int(input())

for tc in range(1, T+1):
    word = [input() for _ in range(5)]
    word_len = []
    for i in word:
        word_len.append(len(i))
    long_word = my_max(word_len)      # 이만큼 가로로 가면서 세로로 5번씩 뽑아내야함
    result = ""
    for i in range(long_word):
        for j in range(5):
            try:
                result += str(word[j][i])
            except:         # 인덱스 오류나면 넘긴다.
                continue
    print(f'#{tc} {result}')

```

### 1859번(다시 풀어봐야됨)

```python
def my_max(a):
    result = 0
    for i in range(len(a)):
        if result < a[i]:
            result = a[i]
    return result

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = my_max(price)   # 제일 비싼가격
    result = 0
    for idx in range(N-1):
        if price[idx] == max_price:
            max_price = my_max(price[idx+1:])
        elif price[idx] < max_price:
            result += max_price - price[idx]
    print(f'#{tc} {result}')

```



