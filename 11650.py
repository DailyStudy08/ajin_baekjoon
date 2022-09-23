import sys
N = int(sys.stdin.readline().strip())
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
for i in sorted_data:
    print(*i)
