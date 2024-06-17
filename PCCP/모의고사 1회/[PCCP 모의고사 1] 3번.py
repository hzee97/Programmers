def algo(n,p):
    if n==1:
        return 'Rr'
    
    val=algo(n-1,(p-1)//4+1)
    case=['RR','Rr','Rr','rr']
    
    if val =='Rr':
        return case[p%4-1]
    else:
        return val
        
def solution(queries):
    answer = []
    
    for n,p in queries:
        answer.append(algo(n,p))
        
    return answer