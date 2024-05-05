def solution(n, times):
    answer = 0
    
    times.sort()
    
    start=min(times)
    end=max(times)*n
    
    while start<=end:
        mid=(start+end)//2
        people=0
        for i in times:
            people+=mid//i
            if people>=n:
                break
        if people<n:
            start=mid+1
        else:
            end=mid-1
            answer=mid
        
    return answer