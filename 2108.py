import sys
N = int(sys.stdin.readline().strip())
arr =[int(sys.stdin.readline().strip()) for _ in range(N)]

arr.sort()
print(round(sum(arr)/N))
print(arr[N//2])

cnt_arr = {}
for i in arr:
    if i in cnt_arr:
        cnt_arr[i] += 1
    else: cnt_arr[i] = 1
cnt_arr = sorted(cnt_arr.items(), key=lambda x:x[1], reverse=True)
if len(cnt_arr) > 1 and cnt_arr[0][1] == cnt_arr[1][1]:
    print(cnt_arr[1][0])
else:
    print(cnt_arr[0][0])

print(max(arr)-min(arr))