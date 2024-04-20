def solution(s):
    stack=[]
    
    for i in s:
        if len(stack)==0:
            if i=='(':
                stack.append(i)
            else:
                return False
        else:
            if i=='(':
                stack.append(i)
            else:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
                    
    if len(stack)==0:
        return True
    else:
        return False