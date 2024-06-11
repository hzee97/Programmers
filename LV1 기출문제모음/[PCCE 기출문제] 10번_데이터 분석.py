# [PCCE 기출문제] 10번_데이터 분석

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    info={'code':0,'date':1,'maximum':2,'remain':3}
    ext_=[]
    for i in data:
        if i[info[ext]]<val_ext:
            ext_.append(i)
    
    ext_.sort(key=lambda x:x[info[sort_by]])
    answer=ext_
    
    return answer