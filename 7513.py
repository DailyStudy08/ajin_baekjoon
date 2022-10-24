import sys
sys.stdin = open('in.txt','r')
T = int(input())
for tc in range(1, T+1):
    print(f'Scenario #{tc}:')
    m = int(input())
    words = [input() for _ in range(m)]
    n = int(input())
    for _ in range(n):
        k, *args = map(int, input().split())
        for i in range(k):
            print(words[args[i]],end='')
        print()
    print()