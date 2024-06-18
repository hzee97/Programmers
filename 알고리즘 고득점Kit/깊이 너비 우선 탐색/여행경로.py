def solution(tickets):
    answer = []
    
    visited=[False]*(len(tickets))
    
    def dfs(v,route):
        if len(route)==len(tickets)+1:
            answer.append(route)
            return
        
        for idx,val in enumerate(tickets):
            if v==val[0] and not visited[idx]:
                visited[idx]=True
                dfs(val[1],route+[val[1]])
                visited[idx]=False
    
    dfs('ICN',['ICN'])
    
    answer.sort()
    answer=answer[0]
    
    return answer