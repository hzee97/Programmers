# 2018 KAKAO BLIND RECRUITMENT

def solution(dartResult):
    answer = 0
    
    power={'S':1,'D':2,'T':3}
    num=''
    score=[]
    for i in dartResult:
        if i.isdigit():
            num+=i
        elif i in power:
            score.append(int(num)**power[i])
            num=''        
        elif i=='*':
            if len(score)>1:
                score[-2]=score[-2]*2
                score[-1]=score[-1]*2
            else:
                score[-1]=score[-1]*2
        elif i=='#':
            score[-1]=score[-1]*(-1)
        
    answer=sum(score)
    
    return answer