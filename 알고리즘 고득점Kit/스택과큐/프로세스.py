def solution(priorities, location):
    answer = 0
    
    queue=[(idx,val) for idx,val in enumerate(priorities)]
    
    while len(queue)>0:
        now=queue.pop(0)
        # any() : list 원소의 값을 필터링 할 때 사용하는 함수.
        if any(now[1]<i[1] for i in queue):
            queue.append(now)
        else:
            answer+=1
            if now[0]==location:
                return answer