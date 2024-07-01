INF = 2147483647
N, q = map(int, input().split())
lazy = []
D = []
results = []
targetArraySize = 0

def initRMQ(nSize):
    n=1
    while n < nSize:
        n *= 2
    for i in range(2*n-1):
        D.append(INF)
        lazy.append(None)
    return n

def lazy_evaluate(k):
    if lazy[k] == None: return
    D[k] = lazy[k]
    if k < targetArraySize - 1:
        lazy[2*k+1] = lazy[k]
        lazy[2*k+2] = lazy[k]
    lazy[k] = None

def query(targetNode, k, l, r):
    lazy_evaluate(k)
    if abs(l-r) == 1 and D[k] is not None:
        return D[k]
    middle = (l+r) // 2
    if targetNode < middle:
        return query(targetNode, k*2+1, l, middle)
    else:
        return query(targetNode, k*2+2, middle, r)

def update(a, b, k, l, r, x):
    lazy_evaluate(k)
    if r <= a or b <= l:
        return
    if a <= l and r <= b:
        lazy[k] = x
        lazy_evaluate(k)
    else:
        update(a, b, k*2+1, l, (l+r)//2, x)
        update(a, b, k*2+2, (l+r)//2, r, x)
        if D[k * 2 + 1] is not None and D[k * 2 + 2] is not None and D[k * 2 + 1] == D[
            k * 2 + 2]:
            D[k] = D[k * 2 + 1]
        else:
            if D[k] is not None:
                D[k] = None
    lazy_evaluate(k)

targetArraySize=initRMQ(N)
for i in range(q):
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        update(inputs[1], inputs[2]+1, 0, 0, targetArraySize, inputs[3])
    if inputs[0] == 1:
        results.append(query(inputs[1], 0, 0, targetArraySize))

for result in results:
    print(result)