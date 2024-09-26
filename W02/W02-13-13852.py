import sys
from collections import deque

def bfs(X, N, K, arr):
    
    visited = [False]*(N+1)
    visited[X] = True

    queue = deque()
    queue.append(X)
    dist = [0]*(N+1)
    result = []

    while queue:
        city = queue.popleft()

        for i in arr[city]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[city] + 1
                if dist[i]==K:
                    result.append(i)
    return result
    
    

def main():
    
    N, M, K, X = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, sys.stdin.readline().split())
        arr[v1].append(v2)
    
    result = bfs(X, N, K, arr)
    if not result:
        print("-1")
    else:
        result.sort()
        print(*result, sep='\n')

if __name__ == "__main__":
    main()