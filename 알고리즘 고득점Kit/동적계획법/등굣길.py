def solution(m, n, puddles):
    answer = 0
    
    r_puddles=[]
    for [i,j] in puddles:
        print([j,i])
        r_puddles.append([j,i])
    
    D=[[0]*(m+1) for i in range(n+1)]
    D[1][1]=1   # 집의 위치
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            if [i,j] in r_puddles:
                D[i][j]=0
            else:
                D[i][j]=(D[i-1][j]+D[i][j-1])%1000000007
    
    answer=D[n][m]
    
    return answer