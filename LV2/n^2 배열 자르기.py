def solution(n, left, right):
    answer = []
    
    for i in range(left,right+1):
        val=max(i//n,i%n)
        answer.append(val+1)
        
    return answer