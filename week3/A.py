import math
INF = 2147483647
D = []
testN = 0
results = []
N, q = map(int, input().split())
#nは要素数
def initRMQ(nSize):
    n=1
    while n < nSize:
        n *= 2
    for i in range(2*n-1):
        D.append(INF)
    return n

def update(k, x):
    k += testN-1
    D[k] = x
    while k > 0:
        k = (k-1)/2
        k = math.floor(k)
        D[k] = min(D[k*2+1], D[k*2+2])

def findMin(a, b):
    return query(a, b+1, 0, 0, testN)

def query(a, b, k, l, r):
    if r <= a or b <= l:
        return INF
    if a <= l and r <= b:
        return D[k]
    vl = query(a, b, k*2+1, l, math.floor((l+r)/2))
    vr = query(a, b, k*2+2, math.floor((l+r)/2), r)
    return min(vl, vr)

testN = initRMQ(N)
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        update(x, y)
    else:
        results.append(findMin(x, y))

for result in results:
    print(result)