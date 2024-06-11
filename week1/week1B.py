v, e = map(int, input().split())
previousPoint = 0
previousList = []
allList = []
state = []
hasCycle = 0
for i in range(v):
    state.append("unvisited")
    allList.append([])
for i in range(e):
    s, t = map(int, input().split())
    allList[s].append(t)
#     if s == previousPoint:
#         previousList.append(t)
#     else:
#         allList[previousPoint] = previousList
#         previousPoint = s
#         previousList = [t]
# allList[previousPoint] = previousList

def dfs(node):
    if state[node] == "visiting":
        return True
    if state[node] == "visited":
        return False
    state[node] = "visiting"
    for neighbor in allList[node]:
        if dfs(neighbor):
            return True
    state[node] = "visited"
    return False

for i in range(v):
    if dfs(i):
        hasCycle = 1

if hasCycle:
    print(1)
else:
    print(0)
