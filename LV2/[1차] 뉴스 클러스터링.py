# 2018 KAKAO BLIND RECRUITMENT

from collections import Counter

def solution(str1, str2):
    answer = 0
    
    # 두 글자씩 끊어서 다중집합의 원소로 만들기.
    # 영문자로 된 글자쌍만 유효.
    str1_set=[]
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_set.append(str1[i:i+2])
                 
    str2_set=[]
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_set.append(str2[i:i+2])
    
    # 모두 대문자로 변환.
    upper_str1_set=[]
    for i in str1_set:
        upper_str1_set.append(i.upper())

    upper_str2_set=[]
    for i in str2_set:
        upper_str2_set.append(i.upper())
 
    # 문자열 개수
    cnt_str1=Counter(upper_str1_set)
    cnt_str2=Counter(upper_str2_set)
    
    # 교집합 개수
    intersection=sum((cnt_str1&cnt_str2).values())
    
    # 합집합 개수
    union=sum((cnt_str1|cnt_str2).values())

    # 두 집합이 모두 공집합인 경우.
    if intersection==0 and union==0:
        answer=65536
    # 그 외.
    else:
        answer=int((intersection/union)*65536)
        
    return answer