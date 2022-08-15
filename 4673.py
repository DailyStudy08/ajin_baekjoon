def d(n):
    return sum([int(i) for i in str(n)]) + n

def sumDn(n):
    A = set()
    for num in range(1,n+1):
        A.add(d(num))
    return A

B = set(i for i in range(1,10001))
print(*sorted(list(B-sumDn(10000))),sep='\n')
