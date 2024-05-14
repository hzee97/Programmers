def solution(n):
    answer = ''
    arr=['1','2','4']
    
    while n:
        n=n-1
        answer=arr[n%3]+answer
        n//=3
        
    return answer