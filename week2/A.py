n, q = map(int, input().split())

nodeList = [0] * n
rank = [0] * n
results = []
for i in range(n):
    nodeList[i] = i

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


for i in range(q):
    query, x, y = map(int, input().split())
    if(query == 0):
        union(x, y)
    else:
        if(findSet(x) == findSet(y)):
            results.append(1)
        else:
            results.append(0)
for result in results:
    print(result)