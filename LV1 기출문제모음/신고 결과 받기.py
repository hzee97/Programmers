# 2022 KAKAO BLIND RECRUITMENT

def solution(id_list, report, k):
    answer = []
    
    # 동일한 유저에 대한 신고 횟수는 1회로 처리.
    report=list(set(report))
    
    report_cnt={}      # id별 신고 당한 횟수.
    report_info={}     # 신고 정보. 
    for i in report:
        from_id,to_id=i.split()
        if to_id not in report_cnt:
            report_cnt[to_id]=1
        else:
            report_cnt[to_id]+=1
        
        if from_id not in report_info:
            report_info[from_id]=[]    
            report_info[from_id].append(to_id)
        else:
            if to_id not in report_info[from_id]:
                report_info[from_id].append(to_id)
            else:
                continue
                
    check=[]
    for i in report_cnt:
        if report_cnt[i]>=k:
            check.append(i)
        
    for i in id_list:
        if i not in report_info:
            answer.append(0)
        else:
            val=0
            for i in report_info[i]:
                if i in check:
                    val+=1
            answer.append(val)
        
    return answer