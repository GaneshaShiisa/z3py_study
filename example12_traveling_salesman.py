'''巡回セールスマン問題
以下の都市の集合と各2都市間の移動コストが与えられたとき、全ての都市をちょうど一度ずつ巡り出発地に戻る巡回路のうちで総移動コストが最小のものを求めろ。
'''
from z3 import *

map = [
    [0, 2, 3, 1, 0, 0],
    [2, 0, 0, 2, 2, 4],
    [3, 0, 0, 2, 2, 3],
    [1, 2, 2, 0, 2, 0],
    [0, 2, 2, 2, 0, 1],
    [0, 4, 3, 0, 1, 0]
]

for total_cost in range(24):
    t_max = 7
    T = [Int("T%s" % i) for i in range(t_max)]
    f = Function('f', IntSort(), IntSort(), IntSort())

    s = Solver()
    s.add([And(1 <= T[i], T[i] <= 6) for i in range(len(T))])
    for i in range(6):
        for j in range(6):
            s.add(f(i+1, j+1) == map[i][j])

    for i in range(len(T)-1):
        s.add(f(T[i], T[i+1]) > 0)

    s.add([Distinct([T[i] for i in range(t_max-1)])])

    s.add(T[0] == 1)
    s.add(T[-1] == 1)

    s.add(Sum([f(T[i], T[i+1]) for i in range(t_max-1)]) < total_cost)

    print("total_cost=" + str(total_cost) + ":")
    print(s.check())
    if s.check() == sat:
        break

m = s.model()
for i in range(len(T)):
    print('T['+str(i)+']='+str(m[T[i]]))

route_cost = [map[m[T[i]].as_long()-1][m[T[i+1]].as_long()-1]
              for i in range(t_max-1)]

print(route_cost, sum(route_cost))
