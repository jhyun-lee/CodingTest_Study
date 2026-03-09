import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
mission_list = list(map(int, input().split()))


dq = deque(range(1, n + 1))

all_count = 0

for target in mission_list:

    while True:
        if dq[0] == target:
                dq.popleft()
                break
        else:
            idx = dq.index(target)

            if idx<=len(dq)//2:
                dq.rotate(-1)
            else:
                dq.rotate(+1)

            all_count+=1



print(all_count)