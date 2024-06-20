# Summer/Winter Coding(~2018)

def solution(dirs):
    answer = 0
    
    x,y=0,0
    visited=set()
    info={'U':[1,0],'D':[-1,0],'R':[0,1],'L':[0,-1]}
    
    for i in dirs:
        dx,dy=info[i]
        
        nx=x+dx
        ny=y+dy
        
        if -5<=nx<=5 and -5<=ny<=5:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            x,y=nx,ny
            
    answer=len(visited)//2
            
    return answer