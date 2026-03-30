import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())


Map = [[] for _ in range(N + 1)]

for i in range(N-1):
    a,b,Dist = map(int, input().split())

    Map[a].append((b,Dist))
    Map[b].append((a,Dist))
    

def bfs(start, target):
    q = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True
    
    while q:
        now, dist = q.popleft()

        if now == target:
            return dist
            
        for neighbor, weight in Map[now]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, dist + weight))
    return 0


for i in range(M):
    a,b = map(int, input().split())

    print(bfs(a,b))
