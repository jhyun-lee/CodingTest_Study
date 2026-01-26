import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
parent = list(range(N + 1))

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))


edges.sort(key=lambda x:  x[2])


# 부모가 무엇인지
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

# 합쳐버려
def Union(a,b):
    a = find(a)
    b = find(b)
    if a>b:
        parent[b] = a
    else:
        parent[a] = b

    
answer = 0 
last=0
for a,b,c in edges:
    if find(a)!= find(b):
        Union(a,b)
        answer+=c
        last = c

print(answer-last)