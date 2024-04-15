# 2018 KAKAO BLIND RECRUITMENT

def solution(cacheSize, cities):
    answer = 0
    
    # LRU 알고리즘 : '가장 오랫동안 참조되지 않은 페이지를 교체' 하는 알고리즘.
    cache=[]
    time=0
    
    for i in cities:
        # 도시이름은 대소문자 구분을 하지않는다. (대문자로 일괄 통일)
        i=i.upper()
        # 캐시사이즈가 0이 경우
        if cacheSize==0:
            time+=5
        else:
            # 같은 page 이름이 cache내에 없는 경우
            if i not in cache:
                # 캐시에 공간이 있는 경우
                if len(cache)<cacheSize:
                    cache.append(i)
                    time+=5
                # 캐시에 공간이 없는 경우
                else:
                    # 캐시에 있는 페이지 중 가장 오랫동안 방문하지 않은 페이지 제거
                    cache.pop(0)
                    cache.append(i)
                    time+=5
            # 같은 page 이름이 cache내에 있는 경우
            else:
                # cache에 있던 해당 page 제거 후, page 등록 
                cache.remove(i)
                cache.append(i)
                time+=1
                
    answer=time
    
    return answer