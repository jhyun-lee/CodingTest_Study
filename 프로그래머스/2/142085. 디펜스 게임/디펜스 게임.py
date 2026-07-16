

# n명가지고 enemy[i] 막기 / 무적권 있음

import heapq
    
def solution(n, k, enemy):
    answer = 0
    
    max_heap = []
    
    for i in range(len(enemy)):
        n -= enemy[i]
        heapq.heappush(max_heap, -enemy[i])
        
        if n < 0:
            if k > 0:
                biggest_enemy = -heapq.heappop(max_heap)
                n += biggest_enemy
                k -= 1  
            else:
                return i
    
    return len(enemy)