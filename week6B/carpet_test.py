MAX = 10
cnt = 0
H = 0
W = 0
limit = 0
maxw = 0
T = [[0] * MAX for _ in range(MAX)]
K = [[0] * MAX for _ in range(MAX)]
C = [[0] * MAX for _ in range(MAX)]
X = [[0] * MAX for _ in range(MAX)]
v = []

def md():
    sum_val = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] and X[i][j] == 0:
                sum_val += 1
    return sum_val // (maxw * maxw)

def dfs(pos, cost):
    global limit
    solved = True
    for i in range(H):
        for j in range(W):
            if C[i][j] and X[i][j] == 0:
                solved = False
    if solved:
        return True
    if pos >= len(v):
        return False
    if cost + md() >= limit:
        return False

    for i in range(v[pos][0] + 1, H):
        for j in range(W):
            if C[i][j] and X[i][j] == 0:
                return False

    tmp = [[0] * MAX for _ in range(MAX)]

    if dfs(pos + 1, cost):
        return True

    for i in range(H):
        for j in range(W):
            tmp[i][j] = X[i][j]
    pi = v[pos][0]
    pj = v[pos][1]
    w = T[pi][pj]
    for y in range(pi - w + 1, pi + 1):
        for x in range(pj - w + 1, pj + 1):
            X[y][x] += 1

    if dfs(pos + 1, cost + 1):
        return True
    for i in range(H):
        for j in range(W):
            X[i][j] = tmp[i][j]

    return False

def idp():
    global limit
    if maxw == 0:
        return 0
    for limit in range(md(), 100):
        if dfs(0, 0):
            return limit

def compute():
    global maxw, cnt
    U = [[True] * MAX for _ in range(MAX)]
    V = [[False] * MAX for _ in range(MAX)]
    global T, K, X

    for i in range(H):
        T[i][0] = 1 if C[i][0] else 0
    for j in range(W):
        T[0][j] = 1 if C[0][j] else 0

    for i in range(1, H):
        for j in range(1, W):
            if C[i][j]:
                T[i][j] = min(T[i-1][j-1], min(T[i-1][j], T[i][j-1])) + 1
            else:
                T[i][j] = 0

    for i in range(H):
        for j in range(W):
            w = T[i][j]
            for pi in range(i - (w - 1), i + 1):
                for pj in range(j - (w - 1), j + 1):
                    if i == pi and j == pj:
                        continue
                    l = max(i - pi, j - pj)
                    if w - l >= T[pi][pj]:
                        U[pi][pj] = False

    for i in range(H):
        for j in range(W):
            if U[i][j] and T[i][j]:
                for y in range(i - T[i][j] + 1, i + 1):
                    for x in range(j - T[i][j] + 1, j + 1):
                        K[y][x] += 1

    v.clear()
    for i in range(H):
        for j in range(W):
            if U[i][j] and T[i][j]:
                f = False
                for y in range(i - T[i][j] + 1, i + 1):
                    for x in range(j - T[i][j] + 1, j + 1):
                        if K[y][x] == 1:
                            f = True
                if f:
                    for y in range(i - T[i][j] + 1, i + 1):
                        for x in range(j - T[i][j] + 1, j + 1):
                            X[y][x] += 1
                    cnt += 1
                    T[i][j] = 0

    maxw = 0
    for i in range(H):
        for j in range(W):
            if T[i][j] > 0 and U[i][j]:
                maxw = max(maxw, T[i][j])
                v.append((i, j))

    v.reverse()

if __name__ == "__main__":
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        C = [list(map(int, input().split())) for _ in range(H)]
        cnt = 0
        compute()
        print(idp() + cnt)
