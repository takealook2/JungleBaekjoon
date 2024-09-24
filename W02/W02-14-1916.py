import sys
import heapq

def dijkstra(start, end, graph, city):
    dist = [float('inf')] * (city + 1)
    dist[start] = 0
    pq = [(0, start)]  # 우선순위 큐 (거리, 도시 번호)

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return dist[end]

def main():
    # 도시의 개수
    city = int(sys.stdin.readline())
    # 버스의 개수
    bus = int(sys.stdin.readline())
    
    # 그래프 초기화
    graph = [[] for _ in range(city + 1)]

    for _ in range(bus):
        source_city, dest_city, cost = map(int, sys.stdin.readline().split())
        graph[source_city].append((dest_city, cost))

    # 출발점과 도착점 입력
    res_source_city, res_dest_city = map(int, sys.stdin.readline().split())
    
    # 다익스트라 알고리즘을 사용하여 최소 비용 계산
    result = dijkstra(res_source_city, res_dest_city, graph, city)
    print(result)

if __name__ == "__main__":
    main()
