A, B = map(int,(input().split()))
C = int(input())

h , M  = divmod((B + C),60)
H = (A + h) % 24

print(H , M)