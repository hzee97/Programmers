def solution(input_string):
    answer = ''
    
    alpha=[]
    for i in input_string:
        if len(alpha)==0:
            alpha.append(i)
        else:
            if alpha[-1]!=i:
                alpha.append(i)
            else:
                continue
        
    set_alpha=set(alpha)
    
    alone=[]   # 외톨이 알파벳
    for i in set_alpha:
        if alpha.count(i)>1:
            alone.append(i)
    
    # 외톨이 알파벳이 없다면 문자열 "N"을 return.
    if len(alone)==0:
        answer+='N'
    # 외톨이 알파벳이 있다면 외톨이 알파벳들을 알파벳순으로 이어 붙이기.
    else:
        alone.sort()
        for i in alone:
            answer+=i
            
    return answer