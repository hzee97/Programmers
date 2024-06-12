# 2021 KAKAO BLIND RECRUITMENT

def solution(new_id):
    answer = ''
    
    # 1단계
    new_id=new_id.lower()

    # 2단계
    check=['-','_','.']
    r=[]
    for i in new_id:
        if (i in check) or (i.isalpha()) or (i.isdigit()):
            continue
        else:
            r.append(i)
    for i in r:
        new_id=new_id.replace(i,'')

    # 3단계
    while '..' in new_id:
        new_id=new_id.replace('..','.')
    
    # 4단계
    if len(new_id)>0:
        if new_id[0]=='.':
            new_id=new_id[1:]
    if len(new_id)>0:
        if new_id[-1]=='.':
            new_id=new_id[:-1]
    
    # 5단계
    if len(new_id)==0:
        new_id+='a'
    
    # 6단계
    if len(new_id)>=16:
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id[:-1]
    
    # 7단계
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id+=new_id[-1]
        
    answer=new_id
    
    return answer