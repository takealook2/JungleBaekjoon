import sys
sys.setrecursionlimit(10**9)

# dfs 실행하는 부분
def dfs(V, arr):
    global count
    visited[V] = True
    for i in arr[V]:
        if not visited[i]:
            dfs(i, arr)
            
# 정점의 개수 N, 간선의 개수 M
N, M = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]
visited = [False]*(N+1)
count = 0

# 간선의 양 끝 점 u, v
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

# 특정한 순서로 방문할 필요가 없을 때는 리스트의 요소들을 굳이 정렬할 필요는 없음
for i in range(N+1):
    arr[i].sort()

# 1번 정점부터 N번 정점까지의 방문을 시도
for i in range(1, N+1):
    if not visited[i]:
        # 하나의 연결 요소 전체를 탐색하는 과정
        dfs(i, arr)
        count+=1


print(count)