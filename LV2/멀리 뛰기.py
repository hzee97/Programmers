def solution(n):
    answer = 0
    
    d=[0]*(n+1)
    d[0]=1
    d[1]=2
    
    for i in range(2,n):
        d[i]=(d[i-1]+d[i-2])%1234567
    
    answer=d[n-1]
    
    return answer