import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = []

if M > 0:
    broken = list(map(int, input().split()))

min_count = abs(N - 100)

for diff in range(min_count): 
    for check_num in [N - diff, N + diff]:
        if check_num < 0:
            continue
        
        st_num = str(check_num)
        possible = True
        for char in st_num:
            if int(char) in broken:
                possible = False
                break
        
        if possible:
            count = len(st_num) + abs(check_num - N)
            min_count = min(min_count, count)
            

print(min_count)