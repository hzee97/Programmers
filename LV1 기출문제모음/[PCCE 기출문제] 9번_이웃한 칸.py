# [PCCE 기출문제] 9번_이웃한 칸

def solution(board, h, w):
    answer = 0
    
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]
    for i in range(4):
        nx=h+dx[i]
        ny=w+dy[i]
        if 0<=nx<len(board) and 0<=ny<len(board):
            if board[nx][ny]==board[h][w]:
                answer+=1
    
    return answer