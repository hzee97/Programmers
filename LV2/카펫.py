def solution(brown, yellow):
    answer = []
    s=brown+yellow
    
    for w in range(s-1,-1,-1):
        if s%w!=0:
            continue
        h=s/w
        y=(w-2)*(h-2)
        b=s-y
    
        if y==yellow and b==brown:
            answer.append(w)
            answer.append(h)
            break
        
    return answer