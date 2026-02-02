import sys
import heapq


input = sys.stdin.readline
N = int(input())
answer = 0

CheckMap = []
ParMap=[i for i in range(N)]

def find_parent(x):
    if ParMap[x] != x:
        ParMap[x] = find_parent(ParMap[x])
    return ParMap[x]


def Union(a,b):
    P_a = find_parent(a)
    P_b = find_parent(b)
    
    if P_a > P_b:
        ParMap[P_a] = P_b
    else:
        ParMap[P_b]= P_a


for i in range(N):
    Cost = list(map(int,input().split()))
    for j in range(i + 1, N):
            CheckMap.append([Cost[j],i,j])



CheckMap.sort()
Count=0

for Now in CheckMap:
    if find_parent(Now[1]) != find_parent(Now[2]):
        Union(Now[1],Now[2])
        answer+=Now[0]
        Count+=1


        if Count == N-1:
            break


print(answer)





