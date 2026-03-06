import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input())
    hax = []
    i = 1
    while True:
        h = i * (2 * i - 1)
        if h > n: break
        hax.append(h)
        i += 1
        
    if n in hax:
        print(1)
        return

    queue = deque([(h, 1) for h in hax])
    visited = [False] * (n + 1)
    for h in hax:
        visited[h] = True

    while queue:
        curr, count = queue.popleft()
        for h in hax:
            next_val = curr + h
            
            if next_val == n:
                print(count + 1)
                return
            
            if next_val < n and not visited[next_val]:
                visited[next_val] = True
                queue.append((next_val, count + 1))

solve()