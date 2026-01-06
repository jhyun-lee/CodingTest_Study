import sys

n, m = map(int, sys.stdin.readline().split())

list_map = []
for i in range(n):
    list_map.append(list(map(int, sys.stdin.readline().strip())))

max_area = 1

def findRec(y, x):
    global max_area

    limit = min(n - y, m - x)

    for Move in range(1, limit):
        if list_map[y][x] == list_map[y + Move][x] == list_map[y][x + Move] == list_map[y + Move][x + Move]:
            area = (Move + 1) * (Move + 1)
            if area > max_area:
                max_area = area

for i in range(n):
    for j in range(m):
        findRec(i, j)

print(max_area)