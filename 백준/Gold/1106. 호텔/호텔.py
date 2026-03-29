import sys
from itertools import combinations

import math
input = sys.stdin.readline

Number,City = map(int,input().split())

Way=[]
max_val = Number + 101
dp = [987654321] * max_val
dp[0] = 0


for i in range(City):
    cost, Person = map(int,input().split())
    Way.append([cost, Person])


for i in range(1,max_val):
    for cost, Person in Way:
        if i - Person >= 0:
            if dp[i]>dp[i-Person]+cost:
                dp[i] = dp[i-Person]+cost

answer = min(dp[Number:])
print(answer)

