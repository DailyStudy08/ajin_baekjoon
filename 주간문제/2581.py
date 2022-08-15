import sys

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

primeN_list = []

def primeN(num):
    if num == 1:
        return False
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
        return True 

for i in range(M,N+1):
    if primeN(i) == True:
        primeN_list.append(i)
    
if primeN_list == []:
    print(-1)
else:
    print(sum(primeN_list))
    print(min(primeN_list))