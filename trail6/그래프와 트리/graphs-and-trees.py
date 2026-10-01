n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

lst = [[] for _ in range(n+1)]

for i in edges:
    u,v = i
    lst[u].append(v)
    lst[v].append(u)

visited = [False for _ in range(n+1)]

def dfs(node):
    visited[node] = True
    node_cnt = 1
    edge_cnt = len(lst[node])  # 현재 노드와 연결된 간선 수 (양방향 고려)

    for next_node in lst[node]:
        if not visited[next_node]:
            sub_node, sub_edge = dfs(next_node)
            node_cnt += sub_node
            edge_cnt += sub_edge

    return node_cnt, edge_cnt


tree_count = 0

# 1번 정점부터 N번 정점까지 순회하며 미방문 정점 탐색
for i in range(1, n + 1):
    if not visited[i]:
        node_cnt, edge_cnt = dfs(i)

        # 무방향 그래프이므로 양쪽에서 센 간선 수를 2로 나누어 실제 간선 수 산출
        actual_edges = edge_cnt // 2

        # 간선의 개수가 (정점 개수 - 1)개이면 트리에 해당
        if actual_edges == node_cnt - 1:
            tree_count += 1

print(tree_count)