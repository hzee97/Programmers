# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    answer = 0
    
    basket=[]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                if len(basket)==0:
                    basket.append(board[j][i-1])
                    board[j][i-1]=0
                    break
                else:
                    if basket[-1]==board[j][i-1]:
                        answer+=2
                        basket.pop()
                        board[j][i-1]=0
                    else:
                        basket.append(board[j][i-1])
                        board[j][i-1]=0
                    break
        
    return answer