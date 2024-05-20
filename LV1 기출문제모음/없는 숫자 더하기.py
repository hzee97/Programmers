# 월간 코드 챌린지 시즌3

def solution(numbers):
    answer = 0
    
    for i in range(10):
        if numbers.count(i)==0:
            answer+=i
            
    return answer