def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])
    print(routes)
    val=routes[0][1]
    answer+=1
    
    for start,end in routes:
        if start > val:
            answer+=1
            val=end
            
    return answer