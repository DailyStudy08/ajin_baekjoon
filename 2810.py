N = int(input()) #자리 수 = 사람 수
holder = len(input().replace('LL','L'))+1 # 커플석은 하나의 자리로 취급하고 컵홀더의 개수 구하기

if N <= holder: #사람수가 컵홀더 수보다 적거나 같을 때
    print(N)
else: # 컵홀더가 사람보다 적을 때
    print(holder)
