from collections import deque
def count_node(nodes, start, exclude_node):
    queue = deque([start])
    count = 0
    visited = []
    while queue:
        curr = queue.popleft()
        count += 1
        visited.append(curr)
        for n in nodes[curr]:
            if n != exclude_node and n not in visited:
                queue.append(n)      
    return count

def solution(n, wires):
    link = {}
    for w in wires:
        link[w[0]] = link.get(w[0], []) + [w[1]]
        link[w[1]] = link.get(w[1], []) + [w[0]]    
    min_costs = []
    for w in wires:
        a = count_node(link,w[0],w[1])
        b = count_node(link,w[1],w[0])
        dist = abs(a-b)
        min_costs.append(dist)     
    return min(min_costs)
