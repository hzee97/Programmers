def solution(money):
    answer = 0
    D=[0]*len(money)
    D2=[0]*len(money)
    
    # 첫번째 집 터는 경우.
    D[0]=money[0]
    D[1]=money[0]
    for i in range(2,len(money)-1):
        D[i]=max(D[i-1],D[i-2]+money[i])
    
    # 첫번째 집 안 터는 경우.
    D2[1]=money[1]
    for i in range(2,len(money)):
        D2[i]=max(D2[i-1],D2[i-2]+money[i])

    answer=max(D[-2],D2[-1])
    
    return answer