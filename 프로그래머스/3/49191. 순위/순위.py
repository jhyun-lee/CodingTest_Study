
def solution(n, results):
    answer = 0

    WinList = [[] for i in range(0,n+1)]
    LoseList = [[] for i in range(0,n+1)] 
    
    results.sort(key=lambda x : x[0])
    
    for A,B in results:
        WinList[A].append(B)
        LoseList[B].append(A)
        
    
    for i in range(1, n + 1):
        win_visited = set()  
        stack = [i]         
        
        while stack:
            current = stack.pop()
            for nxt in WinList[current]:
                if nxt not in win_visited:
                    win_visited.add(nxt)  
                    stack.append(nxt)     

        lose_visited = set()
        stack = [i]
        
        while stack:
            current = stack.pop()
            for nxt in LoseList[current]:
                if nxt not in lose_visited:
                    lose_visited.add(nxt)
                    stack.append(nxt)
                    
                    
        if len(win_visited) + len(lose_visited) == n - 1:
            answer += 1
            
    
    return answer