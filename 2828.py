import sys

N, M = map(int,sys.stdin.readline().split()) # N스크린  M바구니
J = int(sys.stdin.readline().strip()) # 떨어지는 사과 개수
arr = [int(sys.stdin.readline().strip()) for i in range(J)] # 사과 떨어지는 위치

start = 0 # 바구니 시작
end = M # 바구니 끝
cnt = 0 #이동 수

for i in range(len(arr)):
    # 바구니 안에 떨어지면 이동안함
    if start <= arr[i] <= end:  
        cnt += 0
    # 바구니보다 오른쪽에 떨어지면 거리 차이만큼 cnt 더하고 바구니 이동하기
    if end < arr[i] :
        cnt += arr[i] - end
        end = arr[i]       
        start = end - M+1
    # 바구니보다 왼쪽에 떨어지면 거리 차이만큼 cnt 더하고 바구니 이동하기    
    if start > arr[i]:
        cnt += start - arr[i]
        start = arr[i]
        end = start+ M-1
print(cnt)