# 2024 KAKAO WINTER INTERNSHIP

def solution(friends, gifts):
    answer = 0
    
    gifts_info={}
    gifts_val={}
    
    for i in friends:
        gifts_info[i]={}
        gifts_val[i]=0
        
    for i in gifts:
        from_n,to_n=i.split()
        if to_n not in gifts_info[from_n]:
            gifts_info[from_n][to_n]=1
        else:
            gifts_info[from_n][to_n]+=1
        gifts_val[from_n]+=1
        gifts_val[to_n]-=1
        
    cnt=[]
    for i in friends:
        cnt.append(0)
        
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            if friends[j] in gifts_info[friends[i]]:
                a=gifts_info[friends[i]][friends[j]]
            else:
                a=0
            if friends[i] in gifts_info[friends[j]]:
                b=gifts_info[friends[j]][friends[i]]
            else:
                b=0
                
            if a>b:
                cnt[i]+=1
            elif a<b:
                cnt[j]+=1
            else:
                if gifts_val[friends[i]]>gifts_val[friends[j]]:
                    cnt[i]+=1
                elif gifts_val[friends[i]]<gifts_val[friends[j]]:
                    cnt[j]+=1
    
    answer=max(cnt)   
    
    return answer