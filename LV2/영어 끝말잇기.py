def solution(n, words):
    answer = []

    success=[]
    for i in range(len(words)):
        # 끝말잇기 첫단어
        if len(success)==0:
            if len(words[i])>=2:
                success.append(words[i])
            else:
                answer.append(1)
                answer.append(1)
        # 이후
        else:
            # 3번조건. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어로 시작.
            # 4번조건. 이전에 등장한 단어 사용불가.
            # 5번조건. 한글자인 단어 사용불가.
            if (success[-1][-1]==words[i][0]) and (words[i] not in success) and (len(words[i])>=2):
                success.append(words[i])
            else:
                if (i+1)%n==0:
                    answer.append(n)
                    answer.append((i//n)+1)
                    break
                else:
                    answer.append((i+1)%n)
                    answer.append((i//n)+1)
                    break
    
    # 주어진 단어들로 탈락자가 생기지 않는경우.
    if len(success)==len(words):
        answer.append(0)
        answer.append(0)
        
    return answer