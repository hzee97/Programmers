def solution(priorities, location):
    answer = 0
    
    queue=[(idx,val) for idx,val in enumerate(priorities)]
        
    while 1:
        now=queue.pop(0)
        if any(now[1]<i[1] for i in queue):
            queue.append(now)
        else:
            answer+=1
            if now[0]==location:
                return answer