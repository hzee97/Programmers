import heapq

def solution(operations):
    answer = []
    queue=[]
    
    for i in operations:
        op1,op2=i.split()
        op2=int(op2)
        
        if op1=='I':
            heapq.heappush(queue,op2)
        elif op1=='D' and op2==1:
            if len(queue)>0:
                val=max(queue)
                queue.remove(val)
        elif op1=='D' and op2==-1:
            if len(queue)>0:
                heapq.heappop(queue)
    
    if len(queue)==0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max(queue))
        answer.append(heapq.heappop(queue))
        
    return answer