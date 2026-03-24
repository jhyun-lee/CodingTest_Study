import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())


Numlist = [i for i in range(10)]
AllList =[]


for Count in range(1,11):
    SelectList = map(list,combinations(Numlist, Count))
    
    for i in SelectList:
        i.sort(reverse=True)
        AllList.append(int("".join(map(str, i))))

AllList.sort()


if N >= len(AllList):
    print(-1)

else:
    print(AllList[N])
