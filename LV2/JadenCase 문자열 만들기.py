def solution(s):
    
    text=s.split(' ')
    answer=[i.capitalize() for i in text]
        
    return ' '.join(answer)