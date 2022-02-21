# 첫번째 풀이
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


for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    dump_cnt = 0
    while dump_cnt < dump:  # dump 크기만큼 실행해야함
        if boxes[max_idx(boxes)] - boxes[min_idx(boxes)] == 0 or boxes[max_idx(boxes)] - boxes[min_idx(boxes)] == 1:
            break  # 만약 덤프중에 평탄화 끝나면 while문 빠져나오기
        boxes[max_idx(boxes)] -= 1  # 기존 최고높이의 상자의 인덱스를 찾아내서 boxes의 해당 인덱스의 값을 1 줄임
        boxes[min_idx(boxes)] += 1  # 기존 최저높이의 상자의 인덱스를 찾아내서 boxes의 해당 인덱스의 값을 1 늘림
        dump_cnt += 1
    print(f'#{tc} {boxes[max_idx(boxes)] - boxes[min_idx(boxes)]}')


# 다시 풀어봄
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


for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    while N > 0:
        high_box = my_max(boxes)
        low_box = my_min(boxes)
        if high_box - low_box == 0 or high_box - low_box == 1:
            break
        N -= 1
        for i in range(len(boxes)):
            if boxes[i] == high_box:
                boxes[i] -= 1
                break
        for i in range(len(boxes)):
            if boxes[i] == low_box:
                boxes[i] += 1
                break
    gap = my_max(boxes) - my_min(boxes)
    print(f'#{tc} {gap}')