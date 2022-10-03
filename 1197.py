import sys
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

V, E = map(int, sys.stdin.readline().split())
graph = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph.append((C, A-1, B-1))
graph.sort()

parent = [x for x in range(V)]
sumV = 0
for C, A, B in graph:
    if find(A) != find(B):
        union(A, B)
        sumV += C
print(sumV)


