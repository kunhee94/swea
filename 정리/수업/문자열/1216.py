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