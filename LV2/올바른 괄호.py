def solution(s):
    answer = True

    l=0
    r=0
    for i in s:
        if i=='(':
            l+=1
        elif i==')':
            r+=1
        if l<r:
            answer=False
            break
    
    if l==r:
        answer=True
    elif l>r:
        answer=False
            
    return answer