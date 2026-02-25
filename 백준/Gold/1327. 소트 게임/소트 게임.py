import sys
from collections import deque

input = sys.stdin.readline

def solve():
    line1 = input().split()
    if not line1: return
    N, K = map(int, line1)
    
    number_list = list(map(int, input().split()))
    target = tuple(sorted(number_list))
    start_node = tuple(number_list)

    if start_node == target:
        print(0)
        return

    queue = deque([(start_node, 0)])
    visited = set()
    visited.add(start_node)

    while queue:
        current, dist = queue.popleft()

        for i in range(N - K + 1):
            next_list = list(current)
            next_list[i:i+K] = reversed(next_list[i:i+K])
            next_node = tuple(next_list)

            if next_node == target:
                print(dist + 1)
                return

            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, dist + 1))

    print(-1)

solve()