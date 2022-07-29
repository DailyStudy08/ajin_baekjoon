import sys
sys.stdin = open('input.txt','r')

N = int(input())
lst = []
for i in range(N):
        lst.append(int(input()))
for j in sorted(lst):
    print(j)
