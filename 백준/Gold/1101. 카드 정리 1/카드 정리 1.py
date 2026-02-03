import sys

input = sys.stdin.readline
N, M = map(int, input().split())

CardMap = []
for _ in range(N):
    box = list(map(int, input().split()))

    present_colors = [idx for idx, val in enumerate(box) if val > 0]
    CardMap.append(present_colors)


used_colors = set()
move_count = 0

for colors in CardMap:
    if not colors: 
        continue
    
    if len(colors) == 1:
        color = colors[0]
        if color not in used_colors:
            used_colors.add(color) 
            continue
    

    move_count += 1

print(max(0, move_count - 1))