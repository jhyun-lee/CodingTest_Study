import sys
input = sys.stdin.readline

N = int(input())
meetings = []

for _ in range(N):
    s, f = map(int, input().split())
    meetings.append((s, f))


meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for s, f in meetings:
    if s >= last_end_time:
        count += 1
        last_end_time = f

print(count)