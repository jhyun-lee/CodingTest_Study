import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mission_list = list(map(int, input().split()))


save = [i + 1 for i in range(n)]

all_count = 0

for target in mission_list:
    target_idx = save.index(target)
    
    left_dist = target_idx
    right_dist = len(save) - target_idx
    
    if left_dist <= right_dist:
        all_count += left_dist
    else:
        all_count += right_dist
    

    save = save[target_idx:] + save[:target_idx]
    
    save.pop(0)

print(all_count)