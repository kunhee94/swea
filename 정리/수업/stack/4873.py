def del_str(str):
    # 문자열은 변경불가능하니 리스트로 형변환
    target_str = list(str)
    for i in range(len(target_str)-1):
        # 만약 연속으로 나오면 그거 2개 지우고 바로 다시 재귀돌아야하니까
        if target_str[i] == target_str[i+1]:
            del target_str[i+1]
            del target_str[i]
            # 다시 문자열로 바꾸고 재귀에 넣어줌
            return del_str(''.join(target_str))
        # 끝까지 돌았는데 이제 연속이 없으면 길이 출력
    return len(target_str)


T = int(input())

for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {del_str(word)}')