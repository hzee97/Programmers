from collections import deque

def solution(prices):
    answer = []
    queue=deque(prices)
    
    while queue:
        now=queue.popleft()
        time=0
        for i in queue:
            time+=1
            if now>i:
                break
        answer.append(time)
            
    return answer