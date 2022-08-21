S = int(input())
stair = [0]+[int(input()) for _ in range(S)] 

def dp(stair):
    if S == 1:
        return stair[1]
    else:
        score =[0, stair[1], stair[2]+stair[1]]
    
    for i in range(3,S+1):
        score.append(max(stair[i]+stair[i-1]+score[i-3],stair[i]+score[i-2]))

    return score[S]
print(dp(stair))