def solution(participant, completion):
    answer = ''
    
    # 정보 입력.
    info={}
    for i in participant:
        if i not in info:
            info[i]=1
        else:
            info[i]+=1
    
    # 완주자 명단에 있는 선수 제거.
    for i in completion:
        info[i]-=1
    
    # 결과 도출.
    for key,value in info.items():
        if value==1:
            answer+=key
            
    return answer