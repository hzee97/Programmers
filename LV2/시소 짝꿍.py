from collections import Counter

def solution(weights):
    answer = 0
    
    counter=Counter(weights)
    for val,cnt in counter.items():
        if cnt>=2:
            answer+=cnt*(cnt-1)//2
            
    weights=list(set(weights))
    
    for i in weights:
        if i*2/3 in weights:
            answer+=counter[i*2/3]*counter[i]
        if i*2/4 in weights:
            answer+=counter[i*2/4]*counter[i]
        if i*3/4 in weights:
            answer+=counter[i*3/4]*counter[i]
            
    return answer