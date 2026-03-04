import sys

input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True) 

def solve():
    if cranes[0] < boxes[0]:
        print(-1)
        return

    checked = [False] * M
    positions = [0] * N
    
    count = 0 
    minutes = 0 

    while count < M:
        for i in range(N):
            while positions[i] < M:
                idx = positions[i]
                if not checked[idx] and cranes[i] >= boxes[idx]:
                    checked[idx] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        minutes += 1

    print(minutes)

solve()