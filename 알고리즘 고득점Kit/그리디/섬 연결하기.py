# Union-Find
def get_parent(parent,x):
    if parent[x]==x:
        return x
    return get_parent(parent,parent[x])

def union_parent(parent,a,b):
    a=get_parent(parent,a)
    b=get_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def find_parent(parent,a,b):
    a=get_parent(parent,a)
    b=get_parent(parent,b)
    
    if a==b:
        return True
    else:
        return False
    
# Kruskal`s Algorithm
def solution(n, costs):
    answer = 0
    
    parent=[0 for i in range(n)]
    for i in range(n):
        parent[i]=i
        
    costs.sort(key=lambda x:x[2])
    
    for i in costs:
        if find_parent(parent,i[0],i[1])==False:
            union_parent(parent,i[0],i[1])
            answer+=i[2]
            
    return answer