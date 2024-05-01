import heapq
def solution(scoville, K):
    answer = 0
    
    # list를 heap으로 변환.
    heapq.heapify(scoville)
    
    while len(scoville)>1:
        # 가장 맵지 않은 음식의 스코빌 지수 
        first=heapq.heappop(scoville)
        
        if first<K:
            # 두 번째로 맵지 않은 음식의 스코빌 지수
            second=heapq.heappop(scoville)
            heapq.heappush(scoville,first+second*2)
            answer+=1
        else:
            break
    
    if scoville[0]<K:
        return -1
    else:
        return answer