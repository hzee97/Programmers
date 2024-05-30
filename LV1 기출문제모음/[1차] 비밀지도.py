# 2018 KAKAO BLIND RECRUITMENT

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        num=bin(arr1[i] | arr2[i])[2:]
        num=num.zfill(n)
        num=num.replace('1','#')
        num=num.replace('0',' ')
        answer.append(num)
        
    return answer