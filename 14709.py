fox = [[0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 0],
       [0, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0]]
N = int(input())
arr = [[0]*6 for i in range(6)]
for i in range(N):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

if arr == fox:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")