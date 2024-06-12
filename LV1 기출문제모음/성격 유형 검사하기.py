# 2022 KAKAO TECH INTERNSHIP

def solution(survey, choices):
    answer = ''
    
    type={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for i in range(len(choices)):
        if choices[i]<4:
            type[survey[i][0]]+=4-choices[i]
        elif choices[i]>4:
            type[survey[i][1]]+=choices[i]-4
        
    type_key=list(type.keys())
    
    for i in range(0,len(type_key),2):
        if type[type_key[i]]<type[type_key[i+1]]:
            answer+=type_key[i+1]
        elif type[type_key[i]]>type[type_key[i+1]]:
            answer+=type_key[i]
        else:
            answer+=min(type_key[i],type_key[i+1])
            
    return answer