N, K = map(int, input().split())
data = list(map(int, input().split()))
new_data = []
for i in range(N-K+1):
    new_data.append(sum(data[i:i+K]))
print(max(new_data))