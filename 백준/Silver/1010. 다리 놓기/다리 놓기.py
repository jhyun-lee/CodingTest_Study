import sys,math


Count = int(input())

for _ in range(Count):
    N,M = map(int,sys.stdin.readline().split())

    #1. print(math.comb(M, N)) 
    
    D_List=[[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(1, M+1):
        D_List[1][i]=i

    for i in range(2, N+1):
        for j in range(i, M+1):
            D_List[i][j] = D_List[i][j-1] + D_List[i-1][j-1]

    print(D_List[N][M])


