v, e = map(int, input().split())
edges = []
for i in range(e):
    x, y, w = map(int, input().split())
    edges.append([x,y,w])

rank = [0] * v
nodeList = [0] * v
for i in range(v):
    nodeList[i] = i

def kruskal():
    sortedEdges = sorted(edges, key=lambda x: x[2])
    totalCost = 0
    for edge in sortedEdges:
        if findSet(edge[0]) != findSet(edge[1]):
            union(edge[0], edge[1])
            totalCost += edge[2]
    return totalCost


def findSet(nodeNumber):
    if nodeNumber != nodeList[nodeNumber]:
        nodeList[nodeNumber] = findSet(nodeList[nodeNumber])
    return nodeList[nodeNumber]

def union(xNodeNum, yNodeNum):
    link(findSet(xNodeNum), findSet(yNodeNum))

def link(xNodeNum, yNodeNum):
    if rank[xNodeNum] > rank[yNodeNum]:
        nodeList[yNodeNum] = xNodeNum
    else:
        nodeList[xNodeNum] = yNodeNum
        if rank[xNodeNum] == rank[yNodeNum]:
            rank[yNodeNum] = rank[yNodeNum] + 1

print(kruskal())