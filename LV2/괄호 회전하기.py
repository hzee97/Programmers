from collections import deque

def correct(arr):
    stack=[]
    for i in arr:
        if len(stack)==0:
            stack.append(i)
        else:
            if stack[-1]=='(' and i==')':
                stack.pop()
            elif stack[-1]=='[' and i==']':
                stack.pop()
            elif stack[-1]=='{' and i=='}':
                stack.pop()
            else:
                stack.append(i)
                
    if len(stack)==0:
        return True
            
def solution(s):
    answer = -1

    s=deque(s)
    cnt=0
    for i in range(len(s)):
        s.rotate(-1)
        rot_s=list(s)
        if correct(rot_s)==True:
            cnt+=1
    
    answer=cnt
    
    return answer