"""
# 테스트케이스 5 시간초과  (원인 : sum() 의 시간복잡도가 O(N) )

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge=deque([0 for i in range(bridge_length)])
    while bridge:
        answer+=1
        bridge.popleft()
        if len(truck_weights)>0:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)     
        
    return answer
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=deque(0 for i in range(bridge_length))
    truck_weights=deque(truck_weights)
    total_weight=0
    while bridge:
        answer+=1
        total_weight-=bridge[0]
        bridge.popleft()
        if truck_weights:
            if total_weight+truck_weights[0]<=weight:
                total_weight+=truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)     
        
    return answer