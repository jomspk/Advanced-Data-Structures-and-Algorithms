
import math
def hoge():
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    m1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
    m2 = r1 + r2
    m3 = abs(r1-r2)
    if m1 > m2:
        print(4)
    elif m1 == m2:
        print(3)
    elif m3<m1<m2:
        print(2)
    elif(m1 == m3):
        print(1)
    else:
        print(0)

hoge()