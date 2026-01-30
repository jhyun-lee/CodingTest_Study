import sys

while True:
    n,m = map(float, sys.stdin.readline().split())
    if n == 0:
        break

    n,m = int(n),int(m* 100 + 0.5)
    dp = [0 for i in range(m+1)] # 사용한 돈 = 총 칼로리


    for i in range(n):
        Calorie, Price= map(float,sys.stdin.readline().split())

        Calorie,Price = int(Calorie),int(Price * 100 + 0.5)


        for j in range(Price, m + 1):
            if dp[j - Price] + Calorie > dp[j]:
                    dp[j] = dp[j - Price] + Calorie


    print(max(dp))



