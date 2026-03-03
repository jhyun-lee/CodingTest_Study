import sys
import heapq

input = sys.stdin.readline

N = int(input())

ClassList = []

for i in range(N):
    n, s, f = map(int, input().split())
    ClassList.append([s, f])


ClassList.sort() 

heap = [ClassList[0][1]]

for i in range(1, N):
    if heap[0] <= ClassList[i][0]:
        heapq.heappop(heap)
        
    heapq.heappush(heap, ClassList[i][1])

print(len(heap))