def solution(n):
    answer = 0
    
    F=[0,1]
    for i in range(2,n+1):
        F.append((F[i-2]+F[i-1])%1234567)
    
    answer=F[n]
    
    return answer