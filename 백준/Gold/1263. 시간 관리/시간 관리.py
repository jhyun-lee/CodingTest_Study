import sys

n = int(sys.stdin.readline())
hours=[0 for _ in range(24)]

list =[]
for _ in range(n):
    T,S = map(int,sys.stdin.readline().split())
    list.append([T,S])

list.sort(key=lambda x: (-x[1],x[0]))

LastHours = float("inf")

for T,S in list:
    if S >= LastHours:
        LastHours -=T 
    else:
        LastHours = S -T


if LastHours < 0:
    print(-1)
else:
    print(LastHours)