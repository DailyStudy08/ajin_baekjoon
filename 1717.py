import sys
def union(x, y):
    set_data[find_parents(y)] = find_parents(x)

def find_parents(x):
    if set_data[x] == x:
        return x
    p = find_parents(set_data[x])
    set_data[x] = p
    return set_data[x]

N, M = map(int,sys.stdin.readline().split())
set_data = [x for x in range(N+1)]
for _ in range(M):
    C, a, b = map(int, input().split())
    if C == 0:
        union(a, b)
    elif C == 1:
        if find_parents(a) == find_parents(b):
            print('YES')
        else:
            print('NO')

