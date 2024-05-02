from itertools import product

def solution(word):
    answer = 0
    
    alpha=['A','E','I','O','U']
    case=[]
    for i in range(1,6):
        for j in product(alpha,repeat=i):
            case.append(''.join(list(j)))
    
    case.sort()
    
    answer=case.index(word)+1
    
    return answer