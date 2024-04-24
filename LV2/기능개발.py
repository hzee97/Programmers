def solution(progresses, speeds):
    answer = []
    
    period=[]
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            period.append((100-progresses[i])//speeds[i])
        else:
            period.append(((100-progresses[i])//speeds[i])+1)
    
    while len(period)>0:
        val=period[0]
        cnt=0
        for i in period:
            if val>=i:
                cnt+=1
            else:
                break
        answer.append(cnt)
        period=period[cnt:]
        
    return answer