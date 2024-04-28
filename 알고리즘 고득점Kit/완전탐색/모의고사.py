def solution(answers):
    answer = []
    
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    
    result=[0,0,0]
    for idx,val in enumerate(answers):
        if one[idx%len(one)]==val:
            result[0]+=1
        if two[idx%len(two)]==val:
            result[1]+=1
        if three[idx%len(three)]==val:
            result[2]+=1
    
    for i in range(len(result)):
        if result[i]==max(result):
            answer.append(i+1)
            
    return answer