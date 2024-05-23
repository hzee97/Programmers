# 2021 카카오 채용연계형 인턴십

def solution(s):
    answer = 0
    
    info={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    for i in info:
        s=s.replace(i,info[i])
    
    answer=int(s)
    
    return answer