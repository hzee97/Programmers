def solution(arr1, arr2):
    # 문제에서 주어진 조건 : 곱할 수 있는 배열만 주어진다.
    a=len(arr1)
    b=len(arr1[0])
    c=len(arr2[0])
    
    # axb 행렬과 bxc 행렬의 곱은 axc 형태로 나온다.
    answer = [[0 for i in range(c)] for j in range(a)]
    
    # 답 도출
    for i in range(a):
        for j in range(c):
            for k in range(b):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
    
    return answer