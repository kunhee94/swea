T = 10

for tc in range(1, T+1):
    N = int(input())
    strs = input()
    cal = {
        '+' : 1,
        '*' : 2}
    stack = []
    result = ''
    for i in range(N):
        # 숫자면
        if strs[i] not in list(i for i in cal):
            result += strs[i]
        # 연산자면
        else:
            # 스택이 비었거나 stack[-1]의 순위보다 str[i]의 순위가 높을때 push
            if stack == [] or cal[stack[-1]] < cal[strs[i]]:
                stack.append(strs[i])
            # stack[-1]의 순위보다 str[i]의 순위가 낮거나 같을때
            elif cal[stack[-1]] >= cal[strs[i]]:
                # str[i]의 순위가 높을 때 까지 pop하여 출력 높아지면 push
                while True:
                    if stack == [] or cal[stack[-1]] < cal[strs[i]]:
                        stack.append(strs[i])
                        break
                    else:
                        result += stack.pop()
    # 다돌았는데 스택이 안비었다면 빌때 까지 pop하여 출력
    while stack:
        result += stack.pop()
    # 후위 표기법으로 표시하기 끝

    # 계산 시작
    final = 0   # 최종 계산결과
    for j in result:
        # 숫자면 스택에 push
        if j not in cal:
            stack.append(j)
        # 연산자면 스택에서 2연속 pop해서 연산하고 다시 푸시
        elif j == '+':
            a = int(stack.pop()) + int(stack.pop())
            stack.append(a)
        elif j == '*':
            a = int(stack.pop()) * int(stack.pop())
            stack.append(a)
    print(f'#{tc} {stack[0]}')
