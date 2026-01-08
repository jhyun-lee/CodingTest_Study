import sys
import heapq

input = sys.stdin.readline
n, m, x, y = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))


def dijkstra(start):
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)] 

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue

        for next_node, weight in adj[curr_node]:
            distance = curr_dist + weight
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(pq, (distance, next_node))
    return distances


short_distances = dijkstra(y)

for d in short_distances:
    if d * 2 > x:
        print(-1)
        sys.exit()

deliveries = sorted([d for d in short_distances if d > 0])

count = 0
fuel = x

for dist in deliveries:
    round_trip = dist * 2
    if fuel >= round_trip:
        fuel -= round_trip
    else:
        count += 1
        fuel = x - round_trip

print(count + 1)