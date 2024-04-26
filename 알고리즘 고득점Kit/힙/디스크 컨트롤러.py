import heapq

def solution(jobs):
    answer = 0

    # 정렬
    jobs.sort()
    
    num=len(jobs)
    times=[]   # 각 작업이 걸리는 시간
    waiting=[] # [작업처리소요시간, 작업요청시간]
    now_time=0
    while len(times)!=num:            
        while len(jobs)>0 and now_time >= jobs[0][0]:
            val=jobs.pop(0)
            heapq.heappush(waiting,(val[1],val[0]))
        
        # waiting 배열이 비어있는경우 -> 현재시간보다 요청이 늦은 작업들만 남음 -> 현재시간 : 작업의 요청시간
        if len(jobs)>0 and len(waiting)==0:
            val=jobs.pop(0)
            now_time=val[0]
            heapq.heappush(waiting,(val[1],val[0]))
        
        x,y=heapq.heappop(waiting)
        now_time+=x
        times.append(now_time-y)
        
    answer=sum(times)//num
    
    return answer