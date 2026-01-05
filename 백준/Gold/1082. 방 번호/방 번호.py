INF = 5001
n = int(input())
room = list(map(int, input().split()))
m = int(input())

dp=[-INF for _ in range(m+1)]

for i in range(n-1,-1,-1):
    cost=room[i]

    for j in range(cost,m+1):
        dp[j] = max(dp[j-cost]*10+i, i, dp[j])



print(dp[m])