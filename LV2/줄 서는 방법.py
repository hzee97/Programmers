import math

def solution(n, k):
    answer = []
    
    num=[]
    for i in range(1,n+1):
        num.append(i)
        
    while n>0:
        tmp=math.factorial(n-1)
        idx,k=(k-1)//tmp,k%tmp
        answer.append(num.pop(idx))
        n-=1
    
    return answer