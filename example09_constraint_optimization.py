'''制約最適化問題（Constraint Optimization）
5つの品物の価格と価値が以下の表に示されるようになっているとする． 
価格の合計が 15以下で，価値の合計が最大になる品物の組み合わせを求めよ。
品物    価格    価値
品物0   3       4
品物1   4       5
品物2   5       6
品物3   7       8
品物4   9       10
'''
from z3 import *

price = [3, 4, 5, 7, 9]
value = [4, 5, 6, 8, 10]

X = [Int("X%s" % i) for i in range(5)]

for val in range(20):

    s = Solver()
    s.add([And(0 <= X[i], X[i] <= 1) for i in range(5)])
    s.add(Sum([price[i]*X[i] for i in range(5)]) <= 15)
    s.add(Sum([value[i]*X[i] for i in range(5)]) >= val)

    if s.check() == sat:
        print(s.check())
        print(s.model(), val)
    else:
        break
