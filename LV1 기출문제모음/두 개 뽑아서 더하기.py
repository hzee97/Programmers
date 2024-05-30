# 월간 코드 챌린지 시즌1

from itertools import combinations

def solution(numbers):
    answer = []
    
    case=list(combinations(numbers,2))
    
    for i in case:
        answer.append(sum(i))
        
    answer=list(set(answer))
    answer.sort()
    
    return answer