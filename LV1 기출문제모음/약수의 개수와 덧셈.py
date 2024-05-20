# 월간 코드 챌린지 시즌2

def div(num):
    # 약수 개수 구하기.
    cnt=0
    for i in range(1,num+1):
        if num%i==0:
            cnt+=1
    return cnt

def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        # 약수의 개수가 짝수/홀수인 경우로 나누기.
        if div(i)%2==0:
            answer+=i
        else:
            answer-=i
            
    return answer