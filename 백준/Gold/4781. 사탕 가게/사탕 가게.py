import sys

def solve():
    # 입력을 더 빠르게 받기 위한 설정
    input = sys.stdin.read().split()
    if not input:
        return
    
    idx = 0
    while idx < len(input):
        n = int(input[idx])
        # 예산 m에 대해서도 반드시 + 0.5를 해주어야 함
        m = int(float(input[idx + 1]) * 100 + 0.5)
        idx += 2
        
        if n == 0 and m == 0:
            break
            
        # dp[i]는 i원으로 얻을 수 있는 최대 칼로리
        dp = [0] * (m + 1)
        
        for _ in range(n):
            calorie = int(input[idx])
            price = int(float(input[idx + 1]) * 100 + 0.5)
            idx += 2
            
            # Unbounded Knapsack 최적화: price부터 m까지 진행
            for j in range(price, m + 1):
                # 새로운 칼로리 합이 더 크면 갱신
                if dp[j - price] + calorie > dp[j]:
                    dp[j] = dp[j - price] + calorie
        
        # 마지막 m 위치의 값이 최대 칼로리
        print(dp[m])

solve()