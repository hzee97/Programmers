def solution(elements):
    answer = 0
    
    new_elements=elements*2
    num=[]
    for i in range(len(elements)):
        for j in range(len(elements)):
            num.append(sum(new_elements[j:i+j+1]))
    
    answer=len(set(num))
    
    return answer