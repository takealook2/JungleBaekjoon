import sys
import heapq

def dijkstra(start, graph, V):
    # 초기화 부분
    dist = [float('inf')]*(V+1)
    # 시작 노드의 거리를 0으로 설정
    dist[start] = 0
    # 우선순위 큐에 시작노드 추가(w, u)
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue

        # 새로운 거리가 더 짧으면 업데이트하고 우선순위 큐에 추가
        # 간선을 처리하는 반복문
        for dest_v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[dest_v]:
                dist[dest_v] = distance
                heapq.heappush(pq, (distance, dest_v))

    for i in range(1, V+1):
        if dist[i]==float('inf'):
            print("INF")
        else:
            print(dist[i])


def main():

    # 정점 개수 V, 간선 개수 E 입력 받기
    V, E = map(int, sys.stdin.readline().split())

    # 시작 정점 k 입력 받기
    k = int(sys.stdin.readline())

    # 인접 리스트를 만들기 위한 graph 초기화
    graph = [[] for _ in range(V+1)]

    # 총 간선의 개수 만큼 존재
    # u, v, w 입력 받기(시작, 도착, 가중치)
    
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))

    dijkstra(k, graph, V)


if __name__ == "__main__":
    main()