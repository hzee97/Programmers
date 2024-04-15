def solution(people, limit):
    answer = 0
    
    # 정렬
    people.sort()  

    start=0
    end=len(people)-1
    
    while start<=end:
        # 몸무게가 많이 나가는 사람과 적게 나가는 사람 pair
        if people[start]+people[end]<=limit:
            start+=1
            end-=1
        else:
            end-=1
        
        answer+=1
            
    return answer