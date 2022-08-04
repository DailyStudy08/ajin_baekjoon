import sys

L= int(sys.stdin.readline())
S= sorted(list(map(int,sys.stdin.readline().split())))
n= int(sys.stdin.readline())

if n not in S:
    if n > S[0]:
        for i in S:
            if i > n : #오름차순 정렬된 리스트 S에서 요소 i가 n보다 크다면,   
                A ,B = S[S.index(i)-1],i #A는 i의 전 요소, B는 i
                break
        print(len(range(A+1,n+1))*len(range(n,B))-1) 
    else:
        print(len(range(1,n+1))*len(range(n,S[0]))-1)
else: #n이 S에 속할때
    print(0)
