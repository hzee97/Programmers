# 2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    answer = []
    
    num=len(stages)
    info=[]
    for i in range(N):
        cnt=0
        for j in range(len(stages)):
            if i<stages[j]<=i+1:
                cnt+=1
        if cnt==0:
            info.append([0,i+1])
        else:
            info.append([(cnt/num),i+1])
        num-=cnt
    
    info.sort(key=lambda x:(-x[0],x[1]))
    
    for i in info:
        answer.append(i[1])
                
    return answer