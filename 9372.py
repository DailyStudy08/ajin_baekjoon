import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
    print(N-1)
