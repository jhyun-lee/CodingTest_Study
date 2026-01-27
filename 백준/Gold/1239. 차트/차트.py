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

    for i in range(len(listVisit_Num)):
        if listVisit_Num[i] < 50:
            for j in range(i + 1, len(listVisit_Num)):
                if listVisit_Num[i] + 50 == listVisit_Num[j]:
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