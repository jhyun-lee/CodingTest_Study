import sys
n, m = map(int, sys.stdin.readline().split())
lamp_map = [sys.stdin.readline().strip() for _ in range(n)]
k = int(sys.stdin.readline())

max_cnt = 0
for i in range(n):
    zero_count = lamp_map[i].count('0')
    if zero_count <= k and (k - zero_count) % 2 == 0:
        current_row_cnt = 0
        for j in range(n):
            if lamp_map[i] == lamp_map[j]:
                current_row_cnt += 1
        
        max_cnt = max(max_cnt, current_row_cnt)

print(max_cnt)