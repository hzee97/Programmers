def solution(want, number, discount):
    answer = 0

    # 원하는 제품
    wants=[]
    for i in range(len(want)):
        for j in range(number[i]):
            wants.append(want[i])
    
    # 답 도출
    for i in range(len(discount)-9):
        copy_wants=wants.copy()
        for j in discount[i:i+10]:
            if j in copy_wants:
                copy_wants.remove(j)
        if len(copy_wants)==0:
            answer+=1

    return answer