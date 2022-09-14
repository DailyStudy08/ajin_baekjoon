import sys

N = int(sys.stdin.readline().strip())

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(N))