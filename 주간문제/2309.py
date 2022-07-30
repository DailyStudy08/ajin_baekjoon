import sys
sys.stdin = open('input.txt','r')

from itertools import combinations

data =[int(input()) for i in range(9)]

for com in list(combinations(data, 7)):
    if sum(com) == 100:
        for j in sorted(com):
            print(j)
        break