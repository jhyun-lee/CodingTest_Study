import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row_str = input().rstrip()
    for j in range(1, M + 1):
        S[i][j] = int(row_str[j-1]) + S[i-1][j] + S[i][j-1] - S[i-1][j-1]


def get_sum(x1, y1, x2, y2):
    return S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]

ans = 0


for i in range(1, M - 1):
    for j in range(i + 1, M):
        ans = max(ans, get_sum(1,1,N,i) * get_sum(1,i+1,N,j) * get_sum(1,j+1,N,M))


for i in range(1, N - 1):
    for j in range(i + 1, N):
        ans = max(ans, get_sum(1,1,i,M) * get_sum(i+1,1,j,M) * get_sum(j+1,1,N,M))


for i in range(1, M):
    for j in range(1, N):
        ans = max(ans, get_sum(1,1,N,i) * get_sum(1,i+1,j,M) * get_sum(j+1,i+1,N,M))


for i in range(1, M):
    for j in range(1, N):
        ans = max(ans, get_sum(1,i+1,N,M) * get_sum(1,1,j,i) * get_sum(j+1,1,N,i))


for i in range(1, N):
    for j in range(1, M):
        ans = max(ans, get_sum(1,1,i,M) * get_sum(i+1,1,N,j) * get_sum(i+1,j+1,N,M))


for i in range(1, N):
    for j in range(1, M):
        ans = max(ans, get_sum(i+1,1,N,M) * get_sum(1,1,i,j) * get_sum(1,j+1,i,M))

print(ans)