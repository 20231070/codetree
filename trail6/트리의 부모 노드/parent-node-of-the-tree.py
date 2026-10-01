def dfs(node):
    visit[node] = True
    for j in lst[node]:
        if not visit[j]:
            parent[j] = node
            dfs(j)



n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

lst = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)] 
parent = [0 for _ in range(n+1)]



for i in edges:
    u,v = i
    lst[u].append(v)
    lst[v].append(u)

dfs(1)

for i in range(2,n+1):
    print(parent[i])