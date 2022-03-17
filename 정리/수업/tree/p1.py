import sys
sys.stdin = open("input.txt", "r")


def pre_order(n):
    if n:
        result.append(n)
        pre_order(ch1[n])
        pre_order(ch2[n])
    return result
V = int(input())    # 정점의 갯수
E = V - 1   # 간선 갯수
arr = list(map(int, input().split()))
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
result = []
# 루트 찾기
for i in range(1, V+1):
    # 모든 정점을 다찍을수 있는게 루트노드임
    if len(pre_order(i)) == V:
        print(result)
        break
    # 루트 못찾았으면 result 초기화하고 다음 노드가 루트인지 확인
    else:
        result = []

