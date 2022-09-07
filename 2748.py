n = int(input())

memo = [0] * 201
def fibo(N):
    if N < 3:
        return 1
    if not memo[N]:
        memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

result = fibo(90)

print(fibo(n))