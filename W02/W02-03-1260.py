import sys
from collections import deque
# 정점의 개수 N
# 간선의 개수 M
# 탐색을 시작할 정점의 번호 V

def dfs(V, arr):
    visited[V] = True
    print(V, end=' ')

    for i in arr[V]:
        if not visited[i]:
            dfs(i, arr)

def bfs(V, arr):
    queue = deque([V])
    visited[V] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

# for i in range(1, N + 1):
#     arr[i].sort()

print(arr)
# dfs(V, arr)
# print()

# visited = [False]*(N+1)
# bfs(V, arr)
