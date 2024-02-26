def solution(N, road, K):
    result = 0
    tree = [[] for _ in range(N+1)]
    min_cost = [float("inf") for _ in range(N+1)]
    min_cost[1] = 0
    for r in road:
        tree[r[0]].append([r[1], r[2]])
        tree[r[1]].append([r[0], r[2]])
    visited = [0 for _ in range(N+1)]
    def dfs(curr, cost):
        if visited[curr]:
            return
        if min_cost[curr] < cost:
            return
        visited[curr] = 1
        min_cost[curr] = min(min_cost[curr], cost)
        for t in tree[curr]:
            if not visited[t[0]]:
                cost = min_cost[curr] + t[1]
                dfs(t[0], cost)       
        visited[curr] = 0
    dfs(1, 0)
    for m in min_cost:
        if m <= K:
            result += 1
    return result
