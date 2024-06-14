# PCCP 기출문제

def solution(bandage, health, attacks):
    answer = 0
    
    attacks_time=[]
    for i in attacks:
        attacks_time.append(i[0])
        
    val=attacks[len(attacks)-1][0]
    now_health=health   # 현재 체력
    time=1
    cnt=0   # 연속성공횟수
    for i in range(val):         
        if time in attacks_time:
            cnt=0
            for j in attacks:
                if time==j[0]:
                    now_health-=j[1]
            if now_health<=0:
                answer=-1
                return answer
        else:
            cnt+=1
            if cnt==bandage[0]:
                now_health+=bandage[2]
                cnt=0
                if now_health>=health:
                    now_health=health
                    
            if now_health==health:
                pass
            else:
                now_health+=bandage[1]
                if now_health>=health:
                    now_health=health
        time+=1
    
    if now_health<=0:
        answer=-1
    else:
        answer=now_health
        
    return answer