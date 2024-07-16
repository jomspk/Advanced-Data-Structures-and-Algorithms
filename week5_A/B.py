def find_bridges(V, E, edges): 
    import sys 
    sys.setrecursionlimit(200000)  # Increase recursion limit to handle deep recursions 
    from collections import defaultdict 
 
    graph = defaultdict(list) 
    for u, v in edges: 
        graph[u].append(v) 
        graph[v].append(u) 
 
    discovery_time = [-1] * V 
    low = [-1] * V 
    parent = [-1] * V 
    bridges = [] 
    time = [0] 
 
    def dfs(u): 
        discovery_time[u] = low[u] = time[0] 
        time[0] += 1 
 
        for v in graph[u]: 
            if discovery_time[v] == -1:  # v is not visited 
                parent[v] = u 
                dfs(v) 
 
                low[u] = min(low[u], low[v]) 
 
                if low[v] > discovery_time[u]: 
                    bridges.append((min(u, v), max(u, v))) 
            elif v != parent[u]: 
                low[u] = min(low[u], discovery_time[v]) 
 
    for i in range(V): 
        if discovery_time[i] == -1: 
            dfs(i) 
 
    bridges.sort() 
 
    return bridges 
 
# Read input 
V, E = map(int, input().split()) 
edges = [tuple(map(int, input().split())) for _ in range(E)] 
 
# Find and print bridges 
bridges = find_bridges(V, E, edges) 
for u, v in bridges: 
    print(u, v)