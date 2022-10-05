# code1
def combination(n,k,s):
    global cnt
    if k == 0:
        cnt += 1
    else:
        for i in range(s, n-k+1):
            comb[k-1] = lst[i]
            combination(n, k-1, i+1)

N, K = map(int,input().split())
lst = [x for x in range(N)]
cnt = 0
comb = [0] * K
combination(N,K,0)
print(cnt)



# code2 : 팩토리얼 함수
from math import factorial
N, K = map(int, input().split())
result = factorial(N) // (factorial(K)*factorial(N-K))
print(result)



# code3 : 팩토리얼 반복문
def factorial(n):
    if n == 0 :
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
N, K = map(int, input().split())
result = factorial(N) // (factorial(K)*factorial(N-K))
print(result)



# code4 : 팩토리얼 재귀
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
N, K = map(int, input().split())
result = factorial(N) // (factorial(K)*factorial(N-K))
print(result)
