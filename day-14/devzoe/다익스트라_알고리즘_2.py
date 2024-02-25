import heapq

def solution(graph, start):
  distances = {node: float("inf") for node in graph}  
  distances[start] = 0 
  queue = []
  heapq.heappush(queue, [distances[start], start])
  paths = {start: [start]}

  while queue:
    current_distance, current_node = heapq.heappop(queue)

    if distances[current_node] < current_distance:
      continue

    for adjacent_node, weight in graph[current_node].items():
      distance = current_distance + weight

      if distance < distances[adjacent_node]:
        distances[adjacent_node] = distance 
        paths[adjacent_node] = paths[current_node] + [adjacent_node]

        heapq.heappush(queue, [distance, adjacent_node])

  sorted_paths = {node: paths[node] for node in sorted(paths)}

  return [distances, sorted_paths]

graph1 = {'A':{'B':9,'C':3}, 'B':{'A':5}, 'C':{'B':1}}
graph2 = {'A':{'B':1}, 'B':{'C':5}, 'C':{'D':1}, 'D':{}}
start = 'A'
print(solution(graph1, start))
print(solution(graph2, start))
    
