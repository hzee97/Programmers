def solution(n, lost, reserve):
    answer = 0
    
    # 조건1. list 와 reserve 배열에는 중복되는 번호가 없다.
    # 조건2. 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다.
    unique_lost=set(lost)-set(reserve)
    unique_reserve=set(reserve)-set(lost)
    
    for i in unique_reserve:
        # 왼쪽부터 수행.
        if i-1 in unique_lost:
            unique_lost.remove(i-1)
        # 왼쪽 -> 오른쪽 수행
        elif i+1 in unique_lost:
            unique_lost.remove(i+1)
    
    # 답 도출
    answer=n-len(unique_lost)
    
    return answer