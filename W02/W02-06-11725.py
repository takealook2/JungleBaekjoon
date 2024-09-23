import sys
sys.setrecursionlimit(10**6)

def dfs(V, arr, parent):
    visited[V] = True
    for i in arr[V]:
        if not visited[i]:
            parent[i] = V
            dfs(i, arr, parent)

# 트리의 루트는 1
# 노드의 개수 N, 간선의 수는 N-1, 트리 상에서 연결된 두 정점 v1, v2

N = int(sys.stdin.readline())
arr = [[] for i in range(N+1)]
visited = [False]*(N+1)
parent = [0]*(N+1)

for i in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for i in range(N-1):
    arr[i].sort()

dfs(1, arr, parent)

for i in range(2, N+1):
    print(parent[i])