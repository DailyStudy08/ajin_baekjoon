import sys

N = int(sys.stdin.readline().strip()) #테스트케이스 개수

lst = [sys.stdin.readline().split() for _ in range(N)]

sorted_list = sorted(lst, key=lambda x : int(x[0])) 
for i in sorted_list:
    print(*i)
