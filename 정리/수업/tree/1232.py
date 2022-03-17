import sys
sys.stdin = open("input.txt","r")

def back_order(n):
    global back
    if n:
        back_order(int(ch1[n]))
        back_order(int(ch2[n]))
        back.append(tree[n])
for tc in range(1, 11):
    V = int(input())    # 정점 갯수
    tree = [0]*(V + 1)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(V):
        arr = list(input().split())
        tree[i+1] = arr[1]
        if len(arr) == 4:
            ch1[i+1] = arr[2]
            ch2[i+1] = arr[3]
    # 후위 표기해볼까?>
    back = []
    back_order(1)
    # 후위표기식 계산
    stack = []
    for i in back:
        if str.isdigit(i):
            stack.append(float(i))
        else:
            first = stack.pop()
            second = stack.pop()
            if i == '+':
                res = float(second) + float(first)
                stack.append(res)
            elif i == '-':
                res = float(second) - float(first)
                stack.append(res)
            elif i == '*':
                res = float(second) * float(first)
                stack.append(res)
            elif i == '/':
                res = float(second) / float(first)
                stack.append(res)
    print(f'#{tc} {int(stack[0]//1)}')
