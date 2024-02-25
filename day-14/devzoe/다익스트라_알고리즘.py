def solution(graph, start):
    visited = []
    min_costs = [float("inf") for _ in graph.keys()]
    s_node = {s : i for i,s in enumerate(graph.keys())}
    i_node = {i : s for i,s in enumerate(graph.keys())}
    pre_node = [float("inf") for _ in graph.keys()]

    min_costs[s_node[start]] = 0
    pre_node[s_node[start]] = start
    
    for i in range(len(graph.keys())):
        filtered_numbers = [num for i, num in enumerate(min_costs) if i_node[i] not in visited]

        m = min(filtered_numbers)
        
        min_index = min_costs.index(m)

        pre = i_node[min_index]
        for k,v in graph[i_node[min_index]].items():
            if min_costs[s_node[k]] > min_costs[s_node[pre]] + v:
               min_costs[s_node[k]] = min_costs[s_node[pre]] + v
               pre_node[s_node[k]] = pre
        visited.append(pre)

    m = {s : 0 for s in graph.keys()}
    path = {s : [] for s in graph.keys()}

    for i,m_c in enumerate(min_costs):
        m[i_node[i]] = m_c
        curr = i
        path[i_node[i]].append(i_node[curr])
        while True:
            if i_node[curr] == 'A':
                break 
            path[i_node[i]].append(pre_node[curr])
            curr = s_node[pre_node[curr]]
    for key in path:
        path[key] = path[key][::-1]
    return m, path  
        
graph1 = {'A':{'B':9,'C':3}, 'B':{'A':5}, 'C':{'B':1}}
graph2 = {'A':{'B':1}, 'B':{'C':5}, 'C':{'D':1}, 'D':{}}
start = 'A'
print(solution(graph1, start))
print(solution(graph2, start))
    
    
