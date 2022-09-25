##### 문제해결함! #####

import sys

# 다중집합 만들기
def make_set(a): 
    result = []
    # 단어에서 글자 두 개 씩 묶어 result에 넣는다
    for i in range(len(a)-1): 
        if a[i:i+2].isalpha(): #알파벳으로만 이루어졌을때 result에 넣기
            result.append(a[i:i+2])  
    return result 

def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    A = make_set(str1)  
    B = make_set(str2)

    if A and B: #A,B 둘 다 공집합이 아닌 경우 
        cnt = 0 #교집합 길이
        for i in A: 
            if i in B:
                B.remove(i)
                cnt+=1
        answer = cnt/(len(A)+len(B)) # 교집합/합집합
    elif not A and not B : #집합 A와 집합 B가 모두 공집합일 경우
        answer = 1
    return int(answer*65536)

str1 = sys.stdin.readline()
str2 = sys.stdin.readline()