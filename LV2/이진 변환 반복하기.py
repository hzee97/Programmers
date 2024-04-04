def solution(s):
    answer = []
    cnt=0
    zero_cnt=0
    while 1:
        if s=='1':
            break
        # 1번 : s의 모든 0을 제거.
        s=list(s)
        x=''
        for i in s:
            if i=='1':
                x+=i
            else:
                zero_cnt+=1
        # 2번 : s의 길이 = c , c를 2진법으로 표현한 문자열
        s=bin(int(len(x)))[2:]
        cnt+=1
        
    answer.append(cnt)
    answer.append(zero_cnt)
    
    return answer