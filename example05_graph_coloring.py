'''グラフ彩色問題（Graph coloring）
以下のグラフの各頂点に 1 から 3 の数を割り当て， 隣接する頂点の異なるようにせよ．
v1 -- v2
 |  /  |
V3 -- V4
'''
from z3 import *

V = [Int('v%s' % i) for i in range(1, 5)]
edges = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]

s = Solver()
s.add([And(1 <= V[i], V[i] <= 3) for i in range(4)])
for x, y in edges:
    s.add(V[x-1] != V[y-1])

print(s.check())
print(s.model())
