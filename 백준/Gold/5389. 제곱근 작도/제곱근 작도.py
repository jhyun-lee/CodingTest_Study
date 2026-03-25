import sys
from itertools import combinations
import math
input = sys.stdin.readline

N = int(input())


for i in range(N):
    Number = int(input())
    

    best_a = float('inf')
    best_b = 0
    found = False


    for j in range(1, int(math.sqrt(Number)) + 1):

        if Number%j==0:
            A = j
            B = Number//j


            if (B - A) % 2 == 0:
                a = (B - A) // 2
                b = (B + A) // 2
                

                if a < best_a:
                    best_a = a
                    best_b = b
                    found = True

    if found:
        print(f"{best_a} {best_b}")
    else:
        print("IMPOSSIBLE")