def solution(s):
    
    text=s.split(' ')
    answer=[]
    # capitalize() : 맨 첫글자만 대문자로 변환.
    for i in text:
        answer.append(i.capitalize())
       
    return ' '.join(answer)