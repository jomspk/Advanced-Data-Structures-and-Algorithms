class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]
    
n, q = map(int, input().split())
weightUnionFind = WeightedUnionFind(n)
results = []
for i in range(q):
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        weightUnionFind.union(inputs[1], inputs[2], inputs[3])
    else:
        if weightUnionFind.same(inputs[1], inputs[2]):
            result = weightUnionFind.diff(inputs[1], inputs[2])
            results.append(result)
        else:
            results.append("?")
for result in results:
    print(result)