from itertools import permutations

def solution(ability):
    answer = 0
    
    case=list(permutations(ability,len(ability[0])))
    
    for i in range(len(case)):
        score=0
        for j in range(len(case[i])):
            score+=case[i][j][j]
        answer=max(answer,score)
        
    return answer