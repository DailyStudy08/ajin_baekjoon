from itertools import permutations

N, M = map(int, input().split())

cards = list(map(int, input().split()))
arr = permutations(cards, 3)
maxV = 0
for i in arr:
    if sum(i) <= M and maxV < sum(i):
        maxV = sum(i)
print(maxV)