import sys
from itertools import combinations
import math
input = sys.stdin.readline


# 소수인지
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 수식 성립하는지 확인

while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    
    if is_prime(p):
        print("no")
    else:

        if pow(a,p,p) == a:
            print("yes")
        else:
            print("no")
