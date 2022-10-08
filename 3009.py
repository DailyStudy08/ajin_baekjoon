X = []
Y = []
for i in range(3):
    x, y = map(int, input().split())
    if x not in X:
        X.append(x)
    else:
        X.remove(x)
    if y not in Y:
        Y.append(y)
    else:
        Y.remove(y)

print(X[0], Y[0])