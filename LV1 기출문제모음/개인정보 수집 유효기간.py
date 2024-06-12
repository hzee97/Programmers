# 2023 KAKAO BLIND RECRUITMENT

def solution(today, terms, privacies):
    answer = []
    
    y,m,d=map(int,today.split('.'))
    today=y*12*28+m*28+d
    
    info={}
    for i in terms:
        types,period=i.split()
        info[types]=int(period)*28
    
    for idx,val in enumerate(privacies):
        num=idx+1
        date,types=val.split()
        yy,mm,dd=map(int,date.split('.'))
        k=yy*12*28+mm*28+dd
        if k+info[types]-1<today:
            answer.append(num)
            
    return answer