import sys
from heapq import *

n = int(sys.stdin.readline())
Meeting_All=[]

for _ in range(n):
    Meeting = list(map(int, sys.stdin.readline().split()))
    Meeting_All.append(Meeting)

Meeting_All.sort(key = lambda x : x[0])
Clear = [] # 
Finish =[]

for start, end, people in Meeting_All:
    while Clear and Clear[0][0] <= start: # 현재 미팅 시간이 기존에 진행했던 미팅 종료시간보다 큰지
        heappush(Finish, -heappop(Clear)[1]) # 인원 추출 해서 포함시켜버림

    if Finish: # 겹치는게 없다면 여기 다 저장되는데, 이걸이제 Clear에 추가해주면됨
        heappush(Clear, (end, people + -Finish[0]))
    else:# 다 겹친다면 지금껄 시작으로 잡아야함
        heappush(Clear, (end, people))


while Clear: # Clear에 남은것들도 다시 finish에 포함시켜주기
    heappush(Finish, -heappop(Clear)[1])


# 정렬된 값들중 가장 늦게 많은 인원수를 배치한거 출력
print(-Finish[0])