from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    case=list(permutations(dungeons,len(dungeons)))
    
    result=[]
    for i in case:
        hp=k
        cnt=0
        for j in i:
            if j[0]<=hp:
                cnt+=1
                hp-=j[1]
            else:
                break
        result.append(cnt)
    
    answer=max(result)
    
    return answer