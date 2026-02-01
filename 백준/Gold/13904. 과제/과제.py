import sys

N = int(sys.stdin.readline())
DayList =[]

max_day = 0

for _ in range(N):
    d,w = map(int, sys.stdin.readline().split())
    DayList.append([d,w])

    if d > max_day:
         max_day = d


DayList.sort()
dp = [0] * (max_day + 1)
# 끝낼수 있는 과제 갯수  >> 과제 최대 점수


for d, w in DayList:
        for j in range(d, 0, -1):
            if dp[j] < dp[j-1] + w:
                dp[j] = dp[j-1] + w


print(max(dp))



