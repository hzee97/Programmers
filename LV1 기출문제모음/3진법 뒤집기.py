# 월간 코드 챌린지 시즌1

def solution(n):
    answer = ''
    
    while n>0:
        # divmod(n,r) : 몫과 나머지를 리턴하는 내장함수.
        # n : 몫, r : 나머지 
        n,r=divmod(n,3)
        answer+=str(r)
        
    # int(x,n): n진법인 x(str형태)를 10진법으로 변환해주는 함수.
    answer=int(answer,3)
    
    return answer