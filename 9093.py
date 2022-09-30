import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    data = sys.stdin.readline().split()
    for d in data:
        print(d[::-1],end=' ')
    print()