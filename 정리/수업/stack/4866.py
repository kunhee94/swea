T = int(input())

for tc in range(1, 1+T):
    code = input()
    top = -1
    stack = [0]*len(code)
    for i in code:
        # 먼저 ( 나 { 가 나오면 top를 1증가시키고 stack[top]에 저장
        if i == '(':
            top += 1
            stack[top] = '('
        elif i == '{':
            top += 1
            stack[top] = '{'
        # ) 나 } 가 나왔을 때 stack[top]이랑 매칭이되면 stack[top] = 0 하고 top 1감소
        elif i == ')':
            if stack[top] == '(':
                stack[top] = 0
                top -= 1
                # 이때 top가 -2가 되면 여는괄호 없이 닫는 괄호가 나왔단 소리니까 0 출력하고 종료
                if top <= -2:
                    print(f'#{tc} 0')
                    break
            # 매칭이 안되면 끝까지 가던말던 짝이 안맞는단 소리니까 0 출력하고 for문 종료
            else:
                print(f'#{tc} 0')
                break
        elif i == '}':
            if stack[top] == '{':
                stack[top] = 0
                top -= 1
                if top <= -2:
                    print(f'#{tc} 0')
                    break
            else:
                print(f'#{tc} 0')
                break
    # for문을 끝까지 돌았고 정상적으로 모든짝이 맞았으면 stack[0]은 0 이여야 함
    else:
        if stack[0] == 0:
            print(f'#{tc} 1')
        # 아닌 경우 여는 괄호가 닫는괄호보다 많았었단 소리임
        else:
            print(f'#{tc} 0')