import sys
input = sys.stdin.readline
from collections import deque


N = int(input())


time = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    for x in data[1:-1]:
        adj[x].append(i)
        indegree[i] += 1


# 위상 정렬 시작
q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]


while q:
    now = q.popleft()
    for next_node in adj[now]:
        indegree[next_node] -= 1

        dp[next_node] = max(dp[next_node], dp[now] + time[next_node])
        if indegree[next_node] == 0:
            q.append(next_node)




for i in range(1, N + 1):
    print(dp[i])
