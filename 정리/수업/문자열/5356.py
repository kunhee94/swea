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