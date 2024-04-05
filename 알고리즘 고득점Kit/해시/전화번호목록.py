# 정확성: 83.3 , 효율성: 16.7

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            answer=False
            break
        
    return answer