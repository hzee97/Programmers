def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks.sort()
    
    start=1
    end=distance
    
    while start<=end:
        mid=(start+end)//2
        cnt=0   # 제거한 바위 수.
        previous=0   # 이전 바위 위치.
        for i in rocks:
            # 거리(i-previous) 가 mid 보다 작으면, 바위 제거
            if i-previous<mid:
                cnt+=1
                # 제거한 바위 수가 조건 n 개를 넘을 때, break 
                if cnt>n:
                    break
            else:
                previous=i
        
        if cnt<=n:
            start=mid+1
            answer=mid
        else:
            end=mid-1
    
    return answer