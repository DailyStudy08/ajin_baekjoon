import sys
arr = [0]

for i in range(1, 46):
    for j in range(i):
       arr.append(i)

A, B = map(int, sys.stdin.readline().split())
print(sum(arr[A:B+1]))
