def solution(k, tangerine):
    answer = 0
    
    # 사이즈별 귤의 개수
    # size : (사이즈, 귤 개수)
    size={}
    for i in tangerine:
        if i not in size:
            size[i]=1
        else:
            size[i]+=1
    
    # 정렬
    sorted_size=sorted(size.items(), key=lambda item:-item[1])

    # val : 귤 개수만 따로 배열 val에 넣기 
    val=[]
    for i in sorted_size:
        val.append(i[1])

    # 값 도출
    cnt=0
    for i in val:
        cnt+=i
        if cnt>=k:
            answer+=1
            break
        else:
            answer+=1

    return answer