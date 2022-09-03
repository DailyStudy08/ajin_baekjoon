def re(n):
    if n < 2:
        return 1
    else:
        return n*re(n-1)

N = int(input())
print(re(N))