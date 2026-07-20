from collections import deque

def solution(m, n, h, w, drops):

    grid = [[987654321] * n for _ in range(m)]
    
    for idx, (r, c) in enumerate(drops):
        grid[r][c] = idx + 1
        

    def get_sliding_min(arr, k):
        res = []
        q = deque()
        for i, val in enumerate(arr):
            while q and arr[q[-1]] >= val:
                q.pop()
            q.append(i)
            
            if q[0] <= i - k:
                q.popleft()
                
            if i >= k - 1:
                res.append(arr[q[0]])
        return res


    row_min = [get_sliding_min(row, w) for row in grid]
    col_min = [get_sliding_min(col, h) for col in zip(*row_min)]
    
    answer = [0, 0]
    max_safe_time = -1
    
    for r in range(m - h + 1):
        for c in range(n - w + 1):
            if col_min[c][r] > max_safe_time:
                max_safe_time = col_min[c][r]
                answer = [r, c]
                
    return answer