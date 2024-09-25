from collections import deque
import sys

def bfs(N, M, maze):
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1

    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()

        if y == N-1 and x == M-1:
            return visited[y][x]


        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0<= ny < N and 0<= nx < M:
                if maze[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))


def main():
    
    N, M = map(int, sys.stdin.readline().split())
    maze = []

    for _ in range(N):
        line = sys.stdin.readline().strip()
        maze.append([int(char) for char in line])

    result = bfs(N, M, maze)
    print(result)

if __name__ == "__main__":
    main()