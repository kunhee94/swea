import sys
sys.stdin = open("input.txt","r")

# 삽입함수
def inq(n):
    global last
    last += 1
    # 1칸확장해서 거기에 n 저장한 다음
    tree[last] = n
    p = last//2
    c = last
    # 루트노드이거나 부모가 자식보다 작아질 때까지 자리바꾸기 지속
    while 0 < p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        # 자리바꿧으면 부모자리로 자식 올려주고 그자리의 부모로 다시 부모세팅
        c = p
        p = c//2

# 조상 찾아서 더하기
def find_anc(n):
    global s
    if n:
        # 트리의 인덱스 전달
        s += tree[n]
        find_anc(n//2)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    last = 0
    arr = list(map(int, input().split()))
    for i in range(N):
        inq(arr[i])
    s = 0
    find_anc(N)
    print(f'#{tc} {s-tree[N]}')



