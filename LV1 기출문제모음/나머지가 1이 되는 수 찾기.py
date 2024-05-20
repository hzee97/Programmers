# 월간 코드 챌린지 시즌3

def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if n%i==1:
            answer=i
            break
            
    return answer