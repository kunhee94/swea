def DFS(n,input_lis, target_num,s):
    global cnt
    if n == len(input_lis):
        if s == target_num:
            cnt += 1
        return
    DFS(n+1, input_lis, target_num, s + input_lis[n])
    DFS(n+1, input_lis, target_num, s - input_lis[n])



def solution(numbers, target):
    global cnt
    answer = 0
    DFS(0,numbers,target,0)
    answer = cnt
    return answer

cnt = 0