from collections import deque

def solution(n, wires):
    answer =987654321
    
    
    maplist = [[] for i in range(n+1)]
    
    
    for v1,v2 in wires:
        maplist[v1].append(v2)
        maplist[v2].append(v1)
        

    def RemoveWay(v1,v2):
        
        # bfs로 탐색하며, 전체 코스트 구하기 
        
        visit = [0] * (n+1)
        visit[v1] = 1
        
        queue = deque()
        queue.append(v1)
        
        Count = 1
        
        while queue:
            Now = queue.popleft()
            
            for i in maplist[Now]:
                if visit[i]==0 and i!=v2:
                    queue.append(i)
                    Count+=1
                    visit[i]=1
                    
        return Count
        
        
    for v1,v2 in wires:  # 제외 할것
        # v1에서의 v2를 제거할것 
        
        CountCost = RemoveWay(v1,v2)
        count_b = n - CountCost
        
        diff = abs(CountCost - count_b)
        
        # 최솟값 갱신
        if diff < answer:
            answer = diff
            
            
    return answer