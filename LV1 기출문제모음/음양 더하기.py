# 월간 코드 챌린지 시즌2

def solution(absolutes, signs):
    answer = 123456789

    num=[]
    for i in range(len(absolutes)):
        if signs[i]==True:
            num.append(absolutes[i])
        else:
            num.append(absolutes[i]*(-1))

    answer=sum(num)
    
    return answer