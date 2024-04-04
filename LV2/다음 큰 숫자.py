def solution(n):
    answer = 0
    # n을 2진수로 변환했을 때 1의 개수
    bin_n=bin(n)[2:]
    bin_n_cnt=bin_n.count('1')
   
    for i in range(n+1,1000001):
        bin_num=bin(i)[2:]
        bin_num_cnt=bin_num.count('1')
        if bin_n_cnt==bin_num_cnt:
            answer=i
            break
        
    return answer