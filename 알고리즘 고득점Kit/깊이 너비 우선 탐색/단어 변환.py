from collections import deque

def solution(begin, target, words):
    answer = 0
    
    queue=deque([(begin,0)])
    visited=[False]*(len(words))
    
    while queue:
        word,cnt=queue.popleft()
        if word==target:
            answer=cnt
            break
        for i in range(len(words)):
            ccnt=0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j]!=words[i][j]:
                        ccnt+=1
                if ccnt==1:
                    queue.append([words[i],cnt+1])
                    visited[i]=1
                    
    return answer