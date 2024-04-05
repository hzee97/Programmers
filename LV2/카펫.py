def solution(brown, yellow):
    answer = []
    
    s=brown+yellow
    
    for h in range(3,int(s**0.5)+1):
        if s%h!=0:
            continue
        else:
            w=s//h
            if (w-2)*(h-2)==yellow :
                answer.append(w)
                answer.append(h)
                break
        
    return answer