# 2019 카카오 개발자 겨울 인턴십

def conv(s):
    s=s[2:-2]
    s=s.split('},{')
    
    return s

def solution(s):
    answer = []
    s=conv(s)
    
    # 정렬
    s.sort(key=len)
    
    val=[]
    for i in s:
        i=i.split(',')
        i=list(map(int,i))
        for j in i:
            if j not in answer:
                answer.append(j)
                
    return answer