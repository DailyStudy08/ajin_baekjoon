import sys
N = int(sys.stdin.readline())

result = [0]*10001

for i in range(N):
    result[int(sys.stdin.readline())]+=1

for i in range(1,10001):
    for j in range(result[i]):
        print(i)

