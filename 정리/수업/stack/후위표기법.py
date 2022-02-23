T = int(input())

cal_icp = {'+': 1,      # 스택에 넣을때 순위
           '-': 1,
           '/': 2,
           '*': 2,
           '(': 3,
           ')': 0
           }
cal_isp = {'+': 1,      # 스택안에서 순위
           '-': 1,
           '/': 2,
           '*': 2,
           '(': 0,
           ')': 0
           }

cal = list(i for i in cal_isp)

for tc in range(1, T+1):
    strs = input()
    stack = []
    result = ''
    for i in range(len(strs)):
        # 숫자면 출력
        if strs[i] not in cal:
            result += strs[i]
        # 연산자라면
        else:
            # strs[i]가 )라면 (만날때 까지 pop하고 출력
            if strs[i] == ')':
                while True:
                    if stack[-1] != '(':
                        result += stack.pop()
                    else:
                        # ( 만났으면 (을 pop하고 정지
                        stack.pop()
                        break
            # 스택이 비어있거나 스택 top의 isp 순위가 자기의 icp 순위보다 낮을때 push
            elif stack == [] or cal_isp[stack[-1]] < cal_icp[strs[i]]:
                stack.append(strs[i])
            # 스택 top의 isp 순위가 자기의 icp 순위보다 높거나 같다면 낮을때 까지 pop하고 push
            elif cal_isp[stack[-1]] >= cal_icp[strs[i]]:
                while True:
                    if stack != [] and stack[-1] == '(':
                        stack.append(strs[i])
                    elif stack == [] or cal_isp[stack[-1]] < cal_icp[strs[i]]:
                        stack.append(strs[i])
                        break
                    else:
                        result += stack.pop()

    while stack != []:
        result += stack.pop()
    print(f'#{tc} {result}')
