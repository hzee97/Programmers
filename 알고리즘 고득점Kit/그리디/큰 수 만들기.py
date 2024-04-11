def solution(number, k):
    answer = ''
    
    stack=[]
    for i in number:
        if len(stack)==0:
            stack.append(i)
        else:
            while len(stack)>0 and k>0 and stack[-1]<i:
                stack.pop()
                k-=1
            stack.append(i)
                
    if k>0:
        stack=stack[:-k]
    
    answer=''.join(stack)
    
    return answer