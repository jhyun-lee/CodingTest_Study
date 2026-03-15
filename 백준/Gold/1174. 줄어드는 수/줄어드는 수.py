import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

Num_list=[]



digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
for i in range(1, 11):
    for comb in combinations(digits, i):
        num_str = "".join(sorted(comb, reverse=True))
        Num_list.append(int(num_str))

Num_list.sort()


if N > len(Num_list):
    print(-1)

else:
    print(Num_list[N-1])
