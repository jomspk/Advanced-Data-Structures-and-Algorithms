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

def query(a,b, k, l, r):
    if r<= a or b<=l:
        return INF
    lazy_evaluate(k)
    if a<=l and r<=b:
        return D[k]
    vl = query(a,b,k*2+1,l, (l+r)//2)
    vr = query(a,b,k*2+2,(l+r)//2,r)
    return min(vl,vr)

def update(a, b, k, l, r, x):
    lazy_evaluate(k)
    if r <= a or b <= l:
        return
    if a <= l and r <= b:
        lazy[k] = x
    else:
        update(a, b, k*2+1, l, (l+r)//2, x)
        update(a, b, k*2+2, (l+r)//2, r, x)
        D[k] = min(D[k*2+1], D[k*2+2])
    lazy_evaluate(k)

targetArraySize=initRMQ(N)
for i in range(q):
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        update(inputs[1], inputs[2]+1, 0, 0, targetArraySize, inputs[3])
    if inputs[0] == 1:
        results.append(query(inputs[1],inputs[2]+1, 0, 0, targetArraySize))

for result in results:
    print(result)