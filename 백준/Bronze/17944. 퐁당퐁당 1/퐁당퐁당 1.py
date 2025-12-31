import sys

N,T = map(int,sys.stdin.readline().split())
Count=0
Mode=0

for _ in range(T):
    
    if Count==2*N:
        Mode=1
    elif Count==1:
        Mode=0

    if Mode==1:
        Count-=1
    else:
        Count+=1


print(Count)