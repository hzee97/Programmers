def solution(name):
    answer = 0
    
    # 커서 좌우 이동.
    cursor_cnt=len(name)-1
    
    # enumerate : (인덱스,값) 형태로 리턴.
    for idx,val in enumerate(name):
        # 알파벳은 대문자로만 이루어져있음.
        # 알파벳 변경 최솟값 (상하 이동).
        answer+=min(ord(val)-ord('A'),ord('Z')-ord(val)+1)
        
        # 연속된 A 문자열 찾기. (현재 알파벳 다음부터)
        next=idx+1
        for i in range(idx+1,len(name)):
            if name[i]=='A':
                next+=1
            else:
                break
        
        # 3가지 비교 : cursor_cnt , 연속된 A의 왼쪽시작방식, 연속된 A의 오른쪽시작방식.
        cursor_cnt=min([cursor_cnt,2*idx+len(name)-next, idx+2*(len(name)-next)])
    
    # 답 도출.
    answer+=cursor_cnt
    
    return answer