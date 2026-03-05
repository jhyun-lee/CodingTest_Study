import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(V + 1)]

def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]
    
    while parent[x] != root:
        next_node = parent[x]
        parent[x] = root
        x = next_node
        
    return root


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0
edges_count = 0

for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost
        edges_count += 1

        if edges_count == V - 1:
            break

print(answer)