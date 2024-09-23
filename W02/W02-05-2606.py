import sys

def dfs(V, arr):
    global virus
    visited[V] = True
    for i in arr[V]:
        if not visited[i]:
            dfs(i, arr)
            virus+=1


# 컴퓨터의 수 computer
# 컴퓨터의 쌍의 수 num
# 그 다음에는 한 줄씩 연결된 컴퓨터의 번호쌍 c1, c2

computer = int(sys.stdin.readline())
num = int(sys.stdin.readline())
visited = [False]*(computer+1)
virus = 0

arr = [[] for i in range(computer+1)]

for i in range(num):
    c1, c2 = map(int, sys.stdin.readline().split())
    arr[c1].append(c2)
    arr[c2].append(c1)

for i in range(computer+1):
    arr[i].sort()

dfs(1, arr)
print(virus)