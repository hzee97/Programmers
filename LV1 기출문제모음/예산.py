# Summer/Winter Coding(~2018)

def solution(d, budget):
    answer = 0
    
    d.sort()
    
    cost=0
    for i in d:
        cost+=i
        if cost<=budget:
            answer+=1
            
    return answer