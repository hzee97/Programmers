# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)

def solution(lottos, win_nums):
    answer = []
    
    rank={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    zero_cnt=lottos.count(0)
    win_cnt=0
    for i in lottos:
        if i in win_nums:
            win_cnt+=1
    
    answer.append(rank[win_cnt+zero_cnt])
    answer.append(rank[win_cnt])
    
    return answer