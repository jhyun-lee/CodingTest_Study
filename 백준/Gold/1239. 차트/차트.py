import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
RateList = list(map(int, input().split()))

if max(RateList) > 50:
    print(0)
    sys.exit()

visitMap = [0] * N
answer = 0

def Check_Num(listVisit_Num):
    Count = 0
    line_set = set(listVisit_Num) 
    for pos in listVisit_Num:
        if pos < 50 and (pos + 50) in line_set:
            Count += 1
    return Count

def dfs(listVisit_Num):
    global answer

    NowLocation = listVisit_Num[-1]


    if len(listVisit_Num) == N + 1:
        if NowLocation == 100:
            answer = max(Check_Num(listVisit_Num), answer)
        return

    for i in range(N):
        if visitMap[i] != 1:
            visitMap[i] = 1
            listVisit_Num.append(NowLocation + RateList[i])
            dfs(listVisit_Num)
            listVisit_Num.pop()
            visitMap[i] = 0

dfs([0])

print(answer)