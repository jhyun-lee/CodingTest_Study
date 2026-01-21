import sys

n, k = map(int, sys.stdin.readline().split())

answer=0
Count=0

def Checking(Bottle):
    answer =0

    while Bottle:
        answer += Bottle%2
        Bottle = Bottle//2

    return answer
    
while True:
    if Checking(n)<=k:
        break
    Buy = n%2
    Node = n//2

    answer+=(Buy*pow(2,Count))
    n = Node + Buy
    
    Count+=1
    

print(answer)