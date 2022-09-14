import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sumV = 0
sum_list = [0]
for num in nums:
    sumV += num
    sum_list.append(sumV)
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    result = sum_list[end]-sum_list[start-1]
    print(result)