S = input()
result = set()
N = len(S)
for i in range(1, N+1):
    for j in range(i, N+1):
        result.add(S[j-i:j])

print(len(result))