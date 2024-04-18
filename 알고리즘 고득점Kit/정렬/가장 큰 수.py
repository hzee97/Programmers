def solution(numbers):
    answer = ''
    
    # 문자열로 변환
    numbers=list(map(str,numbers))
    
    # 정렬
    numbers.sort(key=lambda x:x*3, reverse=True)
    
    answer+=''.join(numbers)
    answer=str(int(answer))
    
    return answer