def dfs(curr, visited, computers):
        visited[curr] = 1
        for j, value in enumerate(computers[curr]):
            if value and not visited[j]:
                dfs(j, visited, computers)
def solution(n, computers):
    cost = 0
    visited = [0 for _ in range(len(computers))]
    for i,arr in enumerate(computers):
        if not visited[i]:
            dfs(i, visited, computers)
            cost += 1
    return cost
